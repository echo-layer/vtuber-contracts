# Technical Philosophy

## 🧩 Architectural Mindset
The core of `vtuber-contracts` is built on the belief that software should be:
- **Resilient:** Handling failures gracefully.
- **Scalable:** Growing with the data volume.
- **Maintainable:** Easy for new contributors to understand.

## 🛠️ Implementation Choices
We prioritize `Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf` for its unique strengths in Codegen-driven boundary — every vtuber-* repo consumes generated artifacts; breaking changes here trigger CI failures in all downstream consumers before merge..
