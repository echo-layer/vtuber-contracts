# Project Vision

## 🌟 Mission Statement
**Become the canonical typed boundary for the vtuber program — every cross-service value crosses through here, internal and external developers consume the same generated SDKs.**

## 🎯 Primary Objectives
- **Objective 1:** Become the canonical typed boundary for the vtuber program — every cross-service value crosses through here
- **Objective 2:** Publish generated SDKs that internal services and external developers consume from the same source via vtuber-api

## 🔭 Long-term Impact
`vtuber-contracts` aims to solve the following problem:
vtuber-contracts is the build-time source of truth for all inter-service typed boundaries in the vtuber-* program. It defines proto3 schemas for messages such as ConversationDirective, VoiceProfile, and Persona, then runs codegen to publish a Rust crate, Python typed stubs (.pyi), and TypeScript declaration files consumed by every other vtuber-* repo and by the public SDK shipped through vtuber-api.

By leveraging `Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf`, we ensure that our solution is not only functional but also future-proof and high-performing.
