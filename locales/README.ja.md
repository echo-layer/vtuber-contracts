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

[ [English](../README.md) | [ภาษาไทย](./README.th.md) | 日本語 | [简体中文](./README.zh.md) ]

vtuber-contracts は vtuber-* プログラム内の全サービス間型付き境界に対するビルド時ソース・オブ・トゥルース。ConversationDirective / VoiceProfile / Persona 等のメッセージに proto3 スキーマを定義し、codegen で Rust crate・Python 型スタブ (.pyi)・TypeScript 宣言ファイルを生成し、他のすべての vtuber-* リポジトリおよび vtuber-api 経由で公開される SDK に提供する。

## ✨ 特徴 (Features)
- 🚀 **全サービス間メッセージ (ConversationDirective / VoiceProfile / Persona / StreamEvent / ToolCall) の proto3 スキーマを安定したパッケージパスで提供**
- 🛡️ **多言語 codegen パイプライン — Rust crate、Python 型スタブ (.pyi via mypy-protobuf)、TypeScript 宣言ファイル (via ts-proto) を生成**
- 📊 **.proto パッケージ単位の semver を強制 — buf breaking-change リンターを CI のハードゲートとして組み込み**

## 🛠️ クイックスタート (Quick Start)
```bash
# Rust toolchain (rustup) と buf CLI (https://buf.build/docs/installation) をインストールし、cargo build && buf generate を実行すると generated/ 配下に Rust / Python / TypeScript のバインディングが生成される
```

## 🗺️ ナวิゲーション (Navigation)
- 🏗️ **[アーキテクチャ (Architecture)](../ARCHITECTURE.md)**
- 📅 **[ロードマップ (Roadmap)](../ROADMAP.md)**
- 🤝 **[貢献する (Contributing)](../CONTRIBUTING.md)**
- 🌳 **[プロジェクト構造 (Structure)](../STRUCTURE.tree)**

## ⚖️ ライセンス (License)
[MIT](../LICENSE)
