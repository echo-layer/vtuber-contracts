# BrainService Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the `BrainService` gRPC interface in `vtuber.v1` and ensure it is serializable and integrated into the SDK.

**Architecture:** Add a new proto file, update the build script for codegen/serde, and verify with unit tests.

**Tech Stack:** Protobuf, Rust (tonic, pbjson).

---

### Task 1: Define BrainService Proto

**Files:**
- Create: `proto/vtuber/v1/brain.proto`

- [ ] **Step 1: Create brain.proto**

```proto
syntax = "proto3";

package vtuber.v1;

service BrainService {
  rpc PushContext (PushContextRequest) returns (PushContextResponse);
}

message PushContextRequest {
  string session_id = 1;
  string user_id = 2;
  string message = 3;
  map<string, string> metadata = 4;
}

message PushContextResponse {
  bool accepted = 1;
  string request_id = 2;
}
```

- [ ] **Step 2: Lint the proto file**

Run: `buf lint`
Expected: PASS

### Task 2: Update Codegen & Serde Integration

**Files:**
- Modify: `build.rs`

- [ ] **Step 1: Add brain.proto to the list of protos in build.rs**

```rust
    let protos = &[
        // ...
        "proto/vtuber/v1/brain.proto",
    ];
```

- [ ] **Step 2: Build the project to trigger codegen**

Run: `cargo build`
Expected: SUCCESS

### Task 3: Verify with Unit Tests

**Files:**
- Modify: `tests/serde_roundtrip.rs`

- [ ] **Step 1: Add test case for PushContextRequest**

```rust
use vtuber_contracts::vtuber::v1::PushContextRequest;

#[test]
fn test_push_context_request_serde() {
    let mut metadata = std::collections::HashMap::new();
    metadata.insert("source".to_string(), "unit-test".to_string());
    
    let request = PushContextRequest {
        session_id: "session-456".to_string(),
        user_id: "user-789".to_string(),
        message: "Neural activation initiated".to_string(),
        metadata,
    };
    
    let json = serde_json::to_string(&request).unwrap();
    let decoded: PushContextRequest = serde_json::from_str(&json).unwrap();
    
    assert_eq!(request.session_id, decoded.session_id);
    assert_eq!(request.metadata.get("source"), Some(&"unit-test".to_string()));
}
```

- [ ] **Step 2: Run tests**

Run: `cargo test --test serde_roundtrip`
Expected: PASS

### Task 4: Finalize and Cleanup

- [ ] **Step 1: Update STRUCTURE.tree**

Run: `tree -a -I 'node_modules|.git|target' > STRUCTURE.tree`

- [ ] **Step 2: Commit and push**

```bash
git add .
git commit -m "feat: add BrainService and PushContext definitions"
git push origin <current-branch>
```
