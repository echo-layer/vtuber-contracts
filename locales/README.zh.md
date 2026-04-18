<div align="center">

# vtuber-contracts

**Build-time typed interface contracts (proto3) for the vtuber-* program — generates a Rust crate, Python typed stubs, and TypeScript declarations consumed by every other vtuber-* repo to prevent contract drift across 17 services.**

[![CI](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/ci.yml)
[![Security](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml/badge.svg)](https://github.com/echo-layer/vtuber-contracts/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](./)

![Rust LOD](https://img.shields.io/badge/Rust_LOD-0-dea584.svg) ![Total LOD](https://img.shields.io/badge/Total_LOD-0-brightgreen.svg)

[![Rust](https://img.shields.io/badge/Rust-dea584?logo=rust&logoColor=white)](./)

</div>

---

[ [English](../README.md) | [ภาษาไทย](./README.th.md) | [日本語](./README.ja.md) | 简体中文 ]

vtuber-contracts 是 vtuber-* 程序中所有服务间类型化边界的构建期真相源 —— 为 ConversationDirective、VoiceProfile、Persona 等消息定义 proto3 schema,然后通过 codegen 生成 Rust crate、Python 类型存根 (.pyi) 与 TypeScript 声明文件,供所有其他 vtuber-* 仓库以及经由 vtuber-api 发布的公共 SDK 使用。

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
