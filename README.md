<div align="center">

# vtuber-contracts

**Build-time typed interface contracts (proto3) for the vtuber-* program — generates a Rust crate, Mojo bindings (via Pixi + Python interop), and TypeScript declarations consumed by every other vtuber-* repo to prevent contract drift across 17 services.**

[![CI](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml)
[![Security](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](./)

![Rust LOD](https://img.shields.io/badge/Rust_LOD-0-dea584.svg) ![Mojo LOD](https://img.shields.io/badge/Mojo_LOD-0-CC0000.svg) ![Total LOD](https://img.shields.io/badge/Total_LOD-0-brightgreen.svg)

[![Rust](https://img.shields.io/badge/Rust-dea584?logo=rust&logoColor=white)](./) [![Mojo](https://img.shields.io/badge/Mojo-CC0000?logo=mojo&logoColor=white)](./) [![buf](https://img.shields.io/badge/buf-151C3B)](./) [![Pixi](https://img.shields.io/badge/Pixi-F4A02D)](./)

</div>

---

[ English | [ภาษาไทย](./locales/README.th.md) | [日本語](./locales/README.ja.md) | [简体中文](./locales/README.zh.md) ]

vtuber-contracts is the build-time source of truth for all inter-service typed boundaries in the vtuber-* program. It defines proto3 schemas for messages such as ConversationDirective, VoiceProfile, and Persona, then runs codegen to publish three consumer surfaces — a Rust crate (via tonic-build), a Mojo binding package (via Pixi + Python interop, see ADR-004), and TypeScript declarations (via ts-proto) — consumed by every other vtuber-* repo and by the public SDK shipped through vtuber-api.

## ✨ Features

- 🚀 **Feature 1** — proto3 schema for all inter-service messages (ConversationDirective, VoiceProfile, Persona, StreamEvent, ToolCall) under stable package paths
- 🛡️ **Feature 2** — Multi-language codegen pipeline producing a Rust crate, Python typed stubs (.pyi via mypy-protobuf), and TypeScript declaration files (via ts-proto)
- 📊 **Feature 3** — Semver enforcement per .proto package with buf breaking-change linter wired into CI as a hard gate

## 🛠️ Quick Start

```bash
# Install Rust toolchain (rustup) and the buf CLI (https://buf.build/docs/installation), then run cargo build && buf generate to produce Rust, Python, and TypeScript bindings under generated/.
```

## 🗺️ Navigation

- 🏗️ **[Architecture](ARCHITECTURE.md)** — Core design and components.
- 📅 **[Roadmap](ROADMAP.md)** — Project timeline and milestones.
- 🤝 **[Contributing](CONTRIBUTING.md)** — How to join and help.
- 🌳 **[Project Structure](STRUCTURE.tree)** — Full file map.

## ⚖️ License

[MIT](LICENSE)
