# Serde Integration & Private Registry Connection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable Serde derivations for all generated Rust types and configure private Kellnr registry connections for Rust, Python, and NPM.

**Architecture:** Update `build.rs` to inject Serde attributes during codegen and create environment-specific registry config files based on `vtuber-commons` templates.

**Tech Stack:** Rust (tonic, prost, serde), Kellnr Registry, Pixi, GitHub Actions.

---

### Task 1: Update Rust Dependencies

**Files:**
- Modify: `Cargo.toml`

- [ ] **Step 1: Move serde to core dependencies and enable derive feature**
- [ ] **Step 2: Enable serde feature for prost-types**

### Task 2: Inject Serde Attributes in build.rs

**Files:**
- Modify: `build.rs`

- [ ] **Step 1: Update build.rs to use type_attribute for all messages and enums**
- [ ] **Step 2: Run cargo build to verify codegen contains Serialize/Deserialize**

### Task 3: Implement Serde Unit Test

**Files:**
- Create: `tests/serde_roundtrip.rs`

- [ ] **Step 1: Create a test that serializes and deserializes ConversationDirective to/from JSON**
- [ ] **Step 2: Verify the test passes with cargo test**

### Task 4: Configure Private Registry (Kellnr)

**Files:**
- Create: `.cargo/config.toml`
- Create: `pip.conf`
- Create: `.npmrc`
- Modify: `Cargo.toml`

- [ ] **Step 1: Set publish restriction in Cargo.toml**
- [ ] **Step 2: Create registry config files for Cargo, Pip, and NPM using Kellnr URL**

### Task 5: Final Verification

- [ ] **Step 1: Run full test suite (cargo test, pixi run test, buf lint)**
- [ ] **Step 2: Update STRUCTURE.tree and push changes**
