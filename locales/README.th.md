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

[ [English](../README.md) | ภาษาไทย | [日本語](./README.ja.md) | [简体中文](./README.zh.md) ]

vtuber-contracts เป็น build-time source of truth สำหรับ typed boundary ทุกตัวระหว่าง service ในโปรแกรม vtuber-* — นิยาม proto3 schema สำหรับ message อย่าง ConversationDirective, VoiceProfile และ Persona แล้ว codegen ออกเป็น Rust crate, Python typed stub (.pyi), และ TypeScript declaration file ที่ทุก vtuber-* repo รวมถึง public SDK ของ vtuber-api ใช้ร่วมกัน

## ✨ ฟีเจอร์เด่น (Features)
- 🚀 **proto3 schema สำหรับ inter-service message ทั้งหมด (ConversationDirective, VoiceProfile, Persona, StreamEvent, ToolCall) ภายใต้ package path ที่เสถียร**
- 🛡️ **Pipeline การทำ codegen หลายภาษา — Rust crate, Python typed stub (.pyi ผ่าน mypy-protobuf), และ TypeScript declaration file (ผ่าน ts-proto)**
- 📊 **บังคับ semver ต่อ .proto package ด้วย buf breaking-change linter ผูกเข้า CI เป็น hard gate**

## 🛠️ เริ่มต้นใช้งาน (Quick Start)
```bash
# ติดตั้ง Rust toolchain (rustup) และ buf CLI (https://buf.build/docs/installation) จากนั้นรัน cargo build && buf generate เพื่อสร้าง binding ภาษา Rust, Python และ TypeScript ไว้ใต้ generated/
```

## 🗺️ การนำทาง (Navigation)
- 🏗️ **[สถาปัตยกรรม (Architecture)](../ARCHITECTURE.md)**
- 📅 **[แผนงาน (Roadmap)](../ROADMAP.md)**
- 🤝 **[การร่วมพัฒนา (Contributing)](../CONTRIBUTING.md)**
- 🌳 **[โครงสร้างโปรเจกต์ (Structure)](../STRUCTURE.tree)**

## ⚖️ ลิขสิทธิ์ (License)
[MIT](../LICENSE)
