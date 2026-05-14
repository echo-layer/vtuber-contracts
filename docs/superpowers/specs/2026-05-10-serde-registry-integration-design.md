# Design Spec: Serde Integration & Private Registry Connection

## 📝 Overview
This specification details the implementation of Serde support for all generated Rust types and the configuration of the project to use the private Kellnr registry. This ensures that contracts are easily serializable/deserializable for configuration purposes (YAML/TOML/JSON) and can be safely shared across the ecosystem.

## 🔗 Related Issues
- Fixes #6 (Connect to private package registry - Kellnr)
- Fixes #7 (Enable serde derivations for all generated types)

## 🏗️ Architectural Changes

### 1. Rust Serde Derivations (Issue #7)
- **Dependency Update:** Move `serde` with `derive` feature to core dependencies in `Cargo.toml`.
- **Prost Integration:** Enable the `serde` feature for `prost-types` to allow Google types (Timestamp, Struct) to be serialized correctly.
- **Codegen Modification:** Update `build.rs` to use `.type_attribute(".", "#[derive(serde::Serialize, serde::Deserialize)]")`.
- **Convention:** Stick to original snake_case naming for maximum compatibility with existing persona YAMLs.

### 2. Private Registry Configuration (Issue #6)
- **Cargo (Rust):** Create `.cargo/config.toml` pointing to `http://kellnr.cntm.labs:31500/api/v1/crates`.
- **Safety:** Add `publish = ["vtuber-registry"]` to `Cargo.toml` to prevent accidental leaks to public registries.
- **Pip (Python):** Create `pip.conf` with `extra-index-url` pointing to Kellnr and mark it as a trusted host.
- **NPM (Node.js):** Create `.npmrc` with scoped registry `@vtuber` pointing to Kellnr.

## 🧪 Verification Plan
1. **Build Test:** Run `cargo build` and ensure it compiles without errors.
2. **Serde Verification:** Write a unit test in Rust that serializes a `ConversationDirective` to JSON and back.
3. **Registry Verification:** Run `cargo metadata --format-version 1` to ensure registry configuration is recognized.
4. **Consistency Check:** Ensure `buf generate` still produces synced code and passes CI linting.

## ⚖️ Future Considerations
- Transitioning from manual file copying to BSR (Buf Schema Registry) once the initial local registry flow is stabilized.

## 🚀 Phase 2: Automated SDK Publishing (Issue #4)

### 1. Workflow Architecture
- **Trigger:** Git tags matching `v*`.
- **Runner:** `self-hosted` (local lab network).
- **Environment:** Manual mapping of `192.168.1.2` to `kellnr.cntm.labs` within the workflow.

### 2. Multi-Language Publishing Logic
- **Rust:** Uses native `cargo publish` with the pre-configured `vtuber-registry`.
- **Python:** 
    - Generates code via `buf`.
    - Packages as a wheel.
    - Publishes to Kellnr PyPI via `twine`.
- **TypeScript:**
    - Generates code via `buf`.
    - Publishes to Kellnr NPM via `npm publish`.
- **GitHub Packages:** Parallel steps to publish to `ghcr.io` or GitHub's language-specific registries as a fallback.

### 3. Secrets Required
- `KELLNR_TOKEN`: For private registry authentication.
- `GITHUB_TOKEN`: Provided automatically by GitHub Actions.
