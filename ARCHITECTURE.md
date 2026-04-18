# System Architecture

## 🏗️ High-Level Overview
vtuber-contracts is the build-time source of truth for all inter-service typed boundaries in the vtuber-* program. It defines proto3 schemas for messages such as ConversationDirective, VoiceProfile, and Persona, then runs codegen to publish a Rust crate, Python typed stubs (.pyi), and TypeScript declaration files consumed by every other vtuber-* repo and by the public SDK shipped through vtuber-api.

## 🗺️ Component Diagram
> [AI: YOU MUST DRAW A TEXT-BASED MERMAID OR TREE DIAGRAM HERE that represents the specific components of vtuber-contractsbased on the Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf. Show data flow from ingestion to storage.]

## 🛠️ Technology Stack
- **Programming Languages:** [AI: Extract ONLY the languages from Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf]
- **Tooling & Infrastructure:** [AI: Extract libs, frameworks, and tools from Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf]
- **Core Pattern:** Single Source of Truth (one schema, many languages)
- **Strategy:** Codegen-driven boundary — every vtuber-* repo consumes generated artifacts; breaking changes here trigger CI failures in all downstream consumers before merge.

## 🔗 Internal References
- Engineering rules: [PRINCIPLES.md](PRINCIPLES.md)
- Live project map: [STRUCTURE.tree](STRUCTURE.tree)
