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

---

### Task 6: Implement Publishing Workflow

**Files:**
- Create: `.github/workflows/publish.yml`

- [ ] **Step 1: Create publish.yml with Multi-Registry support**

```yaml
name: Publish SDKs

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  publish-rust:
    name: Publish Rust Crate
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - name: Map Kellnr Host
        run: |
          if sudo -n true 2>/dev/null; then
            echo "192.168.1.2 kellnr.cntm.labs" | sudo tee -a /etc/hosts
          fi
      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
      - name: Setup Protoc
        uses: arduino/setup-protoc@v3
      - name: Publish to Kellnr
        env:
          SHARED_TOKEN: ${{ secrets.KELLNR_TOKEN }}
        run: |
          cargo login --registry vtuber-registry "$SHARED_TOKEN"
          cargo publish --registry vtuber-registry --allow-dirty

  publish-python:
    name: Publish Python Stubs
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - name: Map Kellnr Host
        run: |
          if sudo -n true 2>/dev/null; then
            echo "192.168.1.2 kellnr.cntm.labs" | sudo tee -a /etc/hosts
          fi
      - name: Setup buf
        uses: bufbuild/buf-setup-action@v1
        with:
          version: "1.68.4"
      - name: Generate and Publish
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.KELLNR_TOKEN }}
          TWINE_REPOSITORY_URL: http://kellnr.cntm.labs:31500/api/v1/pypi
        run: |
          buf generate
          # TODO: Add python packaging logic here if needed
