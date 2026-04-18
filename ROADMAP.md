# Project Roadmap

## 📅 Timeline
Q2 2026 v0.1 (core message schemas), Q3 2026 v0.2 (SDK publish to crates.io/PyPI/npm), Q4 2026 v1.0 (semver-locked stable contracts)

## 🏁 Milestones
v0.1 base messages and Rust+Python+TS codegen wired, v0.2 SDKs published, v0.5 buf breaking-change CI gate enforced, v1.0 stable API frozen for external consumers

## 🚀 Future Vision
Become the canonical typed boundary for the vtuber program — every cross-service value crosses through here, internal and external developers consume the same generated SDKs.

### Phase 1: Foundation
- [ ] Implement core Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf engine.
- [ ] Set up basic CI/CD in `.github/workflows/ci.yml`.

### Phase 2: Scale
- [ ] Optimize Backward compatibility (semver enforced per .proto package via buf breaking) implementations.
- [ ] Expand connector support.

### Phase 3: Excellence
- [ ] Full security audit per [SECURITY.md](SECURITY.md).
- [ ] Finalize production release.
