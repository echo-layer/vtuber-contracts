# Design Decisions (ADR)

## 💡 Philosophy

vtuber-contracts is the single build-time source of truth for every typed boundary between sibling `vtuber-*` services. Decisions here are load-bearing across 16 downstream consumers, so each ADR is recorded with its full constraint and trade-off context. Rolling log keeps the latest 10 entries per `CLAUDE.md`.

## 📝 Decision Log

### ADR-004: Mojo bindings go through Python interop, not native proto codegen

- **Status:** Accepted — 2026-04-22
- **Context:** The three target consumer surfaces for `vtuber-contracts` are Rust, Mojo, and TypeScript. Rust has tonic-build; TypeScript has ts-proto. Mojo, verified against `https://docs.modular.com/mojo/manual/get-started/` as of 2026-04, has **no** native proto3 codegen, no `buf.build/modular/*` plugin, and no community protobuf library. Its documented path for consuming external schemas is Python interop via `Python.import_module()`.
- **Decision:**
  1. `buf generate` continues to produce Python `_pb2.py` + `.pyi` files under `generated/python/vtuber/v1/`. They are a **build-intermediate** for the Mojo consumer surface — not a publicly advertised Python package. There is no `pyproject.toml`; external Python consumers are out of scope for v0.1.
  2. The Mojo binding ships as a Pixi project (`pixi.toml` at repo root). Pixi pulls `mojo`, `python>=3.11`, and `protobuf` into a single environment so `Python.import_module("vtuber.v1.persona_pb2")` resolves at runtime.
  3. Mojo source lives in `mojo/`. Every proto message gets a thin Mojo struct facade that holds a `PythonObject` — see `mojo/vtuber_contracts.mojo`. The facade is opinionated but minimal: just enough so Mojo consumers do not type `Python.import_module` by hand.
  4. CI runs `pixi run check` and `pixi run test`. The Mojo round-trip test consumes the Python stubs under `PYTHONPATH=generated/python`, proving the interop end-to-end.
- **Consequences:**
  - Pixi is a transitive dependency of every Mojo-consuming repo (`vtuber-brain`, `vtuber-voice`). Rust and TypeScript consumers are unaffected.
  - When Modular ships a native Mojo proto plugin, migration path is: add the plugin to `buf.gen.yaml`, keep the Mojo struct facades (same API surface), drop the Python interop guts. Consumers unchanged.
  - Python `_pb2.py` files are committed under `generated/python/` to keep the `buf generate` drift-check from ADR-003 working. They are regenerated — never hand-edited.
  - The older `get.modular.com` + `mojoproject.toml` install flow is deprecated; `patterns/lang/mojo/ci.yml` was rewritten to use Pixi as part of this ADR.

### ADR-003: `buf breaking` is a non-skippable hard CI gate

- **Status:** Accepted — 2026-04-22
- **Context:** The archived `failures/pandora-code/` repo defined four `.proto` files (`brain.proto`, `voice.proto`, `memory.proto`, `streaming.proto`) but wired no `buf breaking` check into CI. Field renames and removals surfaced at consumer runtime instead of at build time, which was one of the stall paths called out in `failures/codex.md`. Once `vtuber-contracts` publishes a v0.1 tag, 16 sibling repos consume it; a silent breaking change is a 16-repo cascade.
- **Decision:**
  1. `patterns/tools/buf/ci.yml` runs `buf breaking --against <baseline>` on every pull request and every push to a release branch. The job is generated into every repo that has `buf` in its `tech_stack`, not just this one, so downstream consumers also catch drift locally before merging.
  2. The check is **not** optional and **not** a warning. A CI failure here blocks merge.
  3. On the very first commit (no `HEAD~1`) the job self-skips with a `::notice::` — this is the only way out, and it only ever fires once per repo.
  4. Baseline selection: pull requests use the merge base with the PR target branch; direct pushes use `HEAD~1`.
- **Consequences:**
  - Every proto change requires a semver bump captured in a PR. Field-number reuse or tag-incompatible field-type changes fail the build, which is exactly the desired forcing function.
  - Back-compatible additions (new optional fields, new enum variants at the end) pass freely, preserving the fast path for additive evolution.
  - The cost is paid once at setup; from that point on, semver discipline is automatic.

### ADR-002: Director / Performer split as the governing protocol boundary

- **Status:** Accepted — 2026-04-22
- **Context:** pandora-code collapsed the reasoning loop and the speech loop into one service tree (`brain/` + `voice/` in the same repo, tightly coupled via implicit Python calls). The rewrite separates the two into `vtuber-brain` and `vtuber-voice` and defines their only contact surface as a typed proto message.
- **Decision:**
  1. `vtuber-brain` is the **Director**: it owns reasoning, memory, persona selection, tool routing. It emits one and only one outbound message type on each turn: `ConversationDirective`.
  2. `vtuber-voice` is the **Performer**: it owns speech synthesis (PersonaPlex-7B primary, Whisper + Typhoon + XTTS cascade fallback for Thai). It consumes `ConversationDirective` and streams audio chunks back — but the audio-stream shape is explicitly **out of scope** for v0.1 and will be added in the brain↔voice vertical slice.
  3. v0.1 ships exactly three messages that define the Director output: `Persona`, `VoiceProfile`, `ConversationDirective`. A minimal `Director` service with a unary `EmitDirective` rpc is included so tonic / buf service codegen paths are validated end-to-end, but full audio streaming is deferred.
- **Consequences:**
  - New Director outputs (tool calls, stream-control signals, persona-switch commands) attach to `ConversationDirective` or get their own top-level message — never a loose JSON blob crossing the boundary.
  - Brain and voice each evolve their internal stacks (LLM swap, TTS swap) without coordinating, as long as the directive shape holds.
  - If this boundary fails — e.g. the Performer needs context the Director does not know — it is a proto-level change, reviewed under ADR-003's breaking-change gate, not a hidden runtime coupling.

### ADR-001: Package naming and layout (`vtuber.v1` under `proto/vtuber/v1/`)

- **Status:** Accepted — 2026-04-22 (supersedes auto-generated ADR-001)
- **Context:** pandora's protos used bare package names (`package voice;`, `package brain;`) with no version suffix and no namespace. That made it impossible to evolve to a v2 package in parallel without a full rename; it also polluted the global proto namespace across multiple services.
- **Decision:**
  1. Every `.proto` file sits under `proto/vtuber/v1/` and declares `package vtuber.v1;`.
  2. When a message needs a breaking change, a new `proto/vtuber/v2/` directory is added alongside, containing only the messages that broke. Consumers migrate one message at a time. The old v1 schemas stay supported until every consumer has migrated.
  3. All timestamps use `google.protobuf.Timestamp`. No bare int64 milliseconds, no ISO8601 strings. Pandora had two incompatible conventions in the same repo.
  4. All closed-set string fields become proto3 enums with the `_UNSPECIFIED = 0` convention. v0.1 introduces `PersonaId`, `Emotion`, and `AudioFormat` — one per 3-message surface. Further enums (`Platform`, `StreamEventType`) are added per vertical slice, not up front.
- **Consequences:**
  - Side-by-side v1/v2 evolution is mechanical: add v2 directory, add v2 messages, bump consumer at their own pace.
  - Anyone reading a proto knows exactly which version they are on from the package path.
  - Enum fields catch category errors at codegen time instead of at runtime string comparison.

---

*Add new decisions above this line using the standard ADR format.*
