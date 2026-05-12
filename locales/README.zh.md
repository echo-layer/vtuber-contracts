<div align="center">

# vtuber-contracts

**面向 vtuber-* 程序的构建期 proto3 类型化接口契约 —— 生成 Rust crate、Mojo 绑定 (经由 Pixi + Python interop) 与 TypeScript 声明,供 17 个服务统一消费以防止契约漂移**

[![CI](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml)
[![Security](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](./)

![Rust LOD](https://img.shields.io/badge/Rust_LOD-207-dea584.svg) ![Mojo LOD](https://img.shields.io/badge/Mojo_LOD-176-CC0000.svg) ![Total LOD](https://img.shields.io/badge/Total_LOD-4770-brightgreen.svg)

[![Rust](https://img.shields.io/badge/Rust-dea584?logo=rust&logoColor=white)](https://www.rust-lang.org/) [![Mojo](https://img.shields.io/badge/Mojo-CC0000?logo=mojo&logoColor=white)](https://www.modular.com/mojo) [![buf](https://img.shields.io/badge/buf-151C3B)](https://buf.build/) [![Pixi](https://img.shields.io/badge/Pixi-F4A02D)](https://pixi.sh/)

</div>

---

[ [English](../README.md) | [ภาษาไทย](./README.th.md) | [日本語](./README.ja.md) | 简体中文 ]

vtuber-contracts 是 vtuber-* 程序中所有服务间类型化边界的构建期真相源 —— 为 ConversationDirective、VoiceProfile、Persona 等消息定义 proto3 schema,然后通过 codegen 生成三种消费者形态:Rust crate (经由 tonic-build)、Mojo 绑定 (经由 Pixi + Python interop,见 ADR-004) 与 TypeScript 声明 (经由 ts-proto),供所有其他 vtuber-* 仓库以及经由 vtuber-api 发布的公共 SDK 使用。

## ✨ 特性 (Features)
- 🚀 **为所有服务间消息 (ConversationDirective / VoiceProfile / Persona / StreamEvent / ToolCall) 提供稳定 package 路径下的 proto3 schema**
- 🛡️ **多语言 codegen 管线 —— 生成 Rust crate、Python 类型存根 (.pyi via mypy-protobuf) 与 TypeScript 声明文件 (via ts-proto)**
- 📊 **按 .proto package 强制执行 semver —— 将 buf breaking-change linter 作为 CI 硬性闸门**

## 🛠️ 快速开始 (Quick Start)
```bash
# 安装 Rust toolchain (rustup) 与 buf CLI (https://buf.build/docs/installation),然后运行 cargo build && buf generate,即可在 generated/ 目录下生成 Rust / Python / TypeScript 绑定
```

## 🗺️ 导航 (Navigation)
- 🏗️ **[架构 (Architecture)](../ARCHITECTURE.md)**
- 📅 **[路线图 (Roadmap)](../ROADMAP.md)**
- 🤝 **[贡献 (Contributing)](../CONTRIBUTING.md)**
- 🌳 **[项目结构 (Structure)](../STRUCTURE.tree)**

## ⚖️ 许可证 (License)
[MIT](../LICENSE)
