# Design Spec: BrainService & PushContext Definitions

## 📝 Overview
This specification details the formalization of the `BrainService` gRPC interface. This service acts as a typed boundary for sending session context (messages, metadata) from upstream services (like `vtuber-api`) to the central `vtuber-brain` component.

## 🔗 Related Issues
- Fixes #9 (Add BrainService and PushContext definitions)

## 🏗️ Architectural Decisions

### 1. Namespace & Package Consistency
- **Package Name:** `vtuber.v1` (aligned with existing contracts).
- **File Location:** `proto/vtuber/v1/brain.proto`.
- **Reasoning:** Maintains a flat and consistent API structure, making it easier for downstream consumers to discover and use types without nested namespaces.

### 2. Service Definition
- **Service:** `BrainService`
- **RPC:** `PushContext(PushContextRequest) -> PushContextResponse`
- **Data Model:**
    - `PushContextRequest`: Contains `session_id`, `user_id`, `message`, and a `metadata` map.
    - `PushContextResponse`: Returns an `accepted` flag and a `request_id` for tracking.

### 3. Integrated Tooling Support
- **Serde:** The new types will automatically support JSON/YAML serialization via the existing `pbjson` integration in `build.rs`.
- **Registry:** The updated crate including `BrainService` will be published to the internal Kellnr registry.

## 🧪 Verification Plan
1. **Linting:** Run `buf lint` to ensure compliance with the Canonical Protobuf Standard.
2. **Codegen:** Run `cargo build` to verify Rust code generation.
3. **Round-trip Test:** Extend `tests/serde_roundtrip.rs` to include a verification for `PushContextRequest`.
