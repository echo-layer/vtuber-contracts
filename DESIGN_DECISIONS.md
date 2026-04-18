# Design Decisions (ADR)

## 💡 Philosophy
This project uses Architectural Decision Records (ADR) to track significant design choices.

## 📝 Decision Log

### ADR-001: Initial Scaffolding
- **Status:** Accepted
- **Context:** Bootstrapped using MLOps Meta-Repo.
- **Decision:** Use Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf for the core implementation to balance performance and safety.
- **Consequences:** Provides a solid foundation for vtuber-contracts is the build-time source of truth for all inter-service typed boundaries in the vtuber-* program. It defines proto3 schemas for messages such as ConversationDirective, VoiceProfile, and Persona, then runs codegen to publish a Rust crate, Python typed stubs (.pyi), and TypeScript declaration files consumed by every other vtuber-* repo and by the public SDK shipped through vtuber-api..

---
*Add new decisions above this line using the standard ADR format.*
