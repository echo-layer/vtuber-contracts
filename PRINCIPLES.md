# Engineering Principles

These principles guide the development and maintenance of `vtuber-contracts`.

## 🛠️ Core Architecture
- **Single Source of Truth (one schema, many languages):** Our primary architectural guideline to ensure code remains clean and understandable.
- **Backward compatibility (semver enforced per .proto package via buf breaking):** Secondary principle focusing on the specific performance and safety needs of the Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf stack.

## ⚖️ Quality Standards
1. **Uncompromising Safety:** Every line of code must prioritize data integrity and memory safety.
2. **Predictable Performance:** Zero-cost abstractions are preferred over convenience if performance is impacted.
3. **Comprehensive Testing:** No feature is complete without an automated test suite runnable via `cargo test && buf lint && buf breaking --against '.git#branch=main'`.

## 🤝 Collaborative Values
- **Explicit over Implicit:** Code should be self-documenting and intent should be clear.
- **Incremental Excellence:** We value small, high-quality PRs over massive, complex changes.
