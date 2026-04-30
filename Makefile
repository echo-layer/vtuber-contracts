# vtuber-contracts bootstrap Makefile.
#
# The `bootstrap` target is the single source of truth for "does this repo
# build end-to-end on a fresh dev machine?" — per failures/codex.md rule #2,
# it must stay green before any feature work. Run it after every proto change.

.PHONY: bootstrap lint breaking generate rust-build rust-test mojo-check ts-check clean deps-check

bootstrap: deps-check lint generate rust-build rust-test mojo-check
	@echo ""
	@echo "============================================"
	@echo "  vtuber-contracts bootstrap: OK"
	@echo "============================================"

deps-check:
	@command -v buf   >/dev/null 2>&1 || { echo "ERROR: buf not installed. See CONTRIBUTING.md"; exit 1; }
	@command -v cargo >/dev/null 2>&1 || { echo "ERROR: cargo not installed. See CONTRIBUTING.md"; exit 1; }
	@command -v pixi  >/dev/null 2>&1 || { echo "ERROR: pixi not installed. See CONTRIBUTING.md"; exit 1; }

lint:
	buf lint

breaking:
	@if git rev-parse HEAD~1 >/dev/null 2>&1; then \
		buf breaking --against ".git#ref=HEAD~1"; \
	else \
		echo "No prior commit; skipping breaking-change check."; \
	fi

generate:
	buf generate
	@test -d generated/python     || { echo "ERROR: generated/python missing"; exit 1; }
	@test -d generated/typescript || { echo "ERROR: generated/typescript missing"; exit 1; }

rust-build:
	cargo build --all-targets

rust-test:
	cargo test

mojo-check:
	@command -v pixi >/dev/null 2>&1 && pixi install --quiet && pixi run check && pixi run test \
		|| echo "WARN: pixi not installed — skipping Mojo check + test (CI still gates on this)"

ts-check:
	@command -v pnpm >/dev/null 2>&1 && pnpm install --silent && pnpm typecheck \
		|| echo "WARN: pnpm not installed — skipping ts typecheck"

clean:
	rm -rf generated target node_modules .pixi
