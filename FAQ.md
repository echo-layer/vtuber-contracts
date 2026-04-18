# Frequently Asked Questions (FAQ)

## ❓ General
**Q: What is vtuber-contracts?**
A: Build-time typed interface contracts (proto3) for the vtuber-* program — generates a Rust crate, Python typed stubs, and TypeScript declarations consumed by every other vtuber-* repo to prevent contract drift across 17 services.

## 🛠️ Technical
**Q: How do I run tests?**
A: Use the command: `cargo test && buf lint && buf breaking --against '.git#branch=main'`.

**Q: Which languages are supported?**
A: Primarily Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf.

## 🤝 Contributing
**Q: How can I help?**
A: Check out [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get involved!
