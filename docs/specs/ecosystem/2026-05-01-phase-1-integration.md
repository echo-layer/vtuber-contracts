# Phase 1: Ecosystem Integration & Asset Schemas

## 📝 Overview
This specification covers the initial integration of core contracts and the adoption of the Ecosystem Interaction Protocol.

## 🔗 Related Issues
- Fixes #1 (Assets JSON Schemas)
- Fixes #2 (Ecosystem Interaction Protocol)
- Closes #5 (Distributed Model for Image Generation)

## 🏗️ Architectural Changes
### 1. Centralized Asset Schemas (Issue #1)
Defined `proto/vtuber/v1/assets.proto` to serve as the source of truth for:
- Persona Identity & Personality
- Voice Profile Configurations
- Model Registry & Allowlist

### 2. Ecosystem Interaction Protocol (Issue #2)
Updated `GEMINI.md` and `CLAUDE.md` with rules for multi-repo coordination:
- No direct cross-repo modifications.
- Issue-based communication for dependency changes.
- Local spec drafting in `docs/specs/ecosystem/`.

### 3. Distributed Model for Image Generation (Issue #5)
- Handled transition of `image.proto` ownership.
- Removed local copy in `vtuber-contracts` to avoid drift, allowing `vtuber-image` to own its implementation-specific contract while keeping `vtuber-contracts` as the SDK publisher.

## ✅ Verification Results
- All proto files linted and verified via `buf`.
- Rust, Python, and TypeScript SDKs regenerated.
- Mojo round-trip tests passing with Thai Unicode support.
