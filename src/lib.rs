//! Typed interface contracts for the vtuber-* program.
//!
//! All messages and services are generated from `proto/vtuber/v1/` at build
//! time via `tonic-build`. Downstream `vtuber-*` crates depend on this crate
//! and use `vtuber_contracts::vtuber::v1::*` — see DESIGN_DECISIONS.md for
//! the package versioning scheme (ADR-001).

pub mod vtuber {
    pub mod v1 {
        tonic::include_proto!("vtuber.v1");
        include!(concat!(env!("OUT_DIR"), "/vtuber.v1.serde.rs"));
    }
}

pub use vtuber::v1;
