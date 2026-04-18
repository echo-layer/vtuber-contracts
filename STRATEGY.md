# Project Strategy

## 🎯 Strategic Intent
Our goal is to build `vtuber-contracts` as a leader in the Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf ecosystem by focusing on:
**Codegen-driven boundary — every vtuber-* repo consumes generated artifacts; breaking changes here trigger CI failures in all downstream consumers before merge.**

## 🗺️ Execution Pillars
1. **Rapid Prototyping:** Iterating quickly while maintaining core architectural integrity.
2. **Community Feedback:** Using user insights to drive the roadmap.
3. **Automation First:** Every repetitive task should be a script or a workflow.

## 📈 Success Metrics
- **Performance:** Achievement of benchmarks defined in `ARCHITECTURE.md`.
- **Stability:** Passing all tests in `cargo test && buf lint && buf breaking --against '.git#branch=main'`.
- **Adoption:** Clear documentation and easy onboarding per `README.md`.
