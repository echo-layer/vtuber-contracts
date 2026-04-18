# Troubleshooting Guide

## 🔍 Common Issues

### Issue: Installation Fails
- **Check:** Ensure your `Rust, Protobuf (proto3), buf, tonic, ts-proto, mypy-protobuf` version matches the requirements.
- **Fix:** Run `cargo build && buf generate` with administrative privileges if necessary.

### Issue: Tests are failing
- **Check:** Verify your environment variables.
- **Run:** `cargo test && buf lint && buf breaking --against '.git#branch=main'` with verbose logging enabled.

## 🛠️ Debugging Tools
Use the built-in logging and diagnostic flags to trace the execution flow.
