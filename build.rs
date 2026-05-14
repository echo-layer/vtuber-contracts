use std::env;
use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let descriptor_path = PathBuf::from(env::var("OUT_DIR").unwrap()).join("proto_descriptor.bin");

    let protos = &[
        "proto/vtuber/v1/conversation.proto",
        "proto/vtuber/v1/voice_profile.proto",
        "proto/vtuber/v1/persona.proto",
        "proto/vtuber/v1/tool_call.proto",
        "proto/vtuber/v1/assets.proto",
        "proto/vtuber/v1/brain.proto",
    ];

    tonic_build::configure()
        .file_descriptor_set_path(&descriptor_path)
        .extern_path(".google.protobuf.Timestamp", "::pbjson_types::Timestamp")
        .extern_path(".google.protobuf.Struct", "::pbjson_types::Struct")
        .compile_protos(protos, &["proto"])?;

    let descriptor_set = std::fs::read(&descriptor_path)?;
    pbjson_build::Builder::new()
        .register_descriptors(&descriptor_set)?
        .build(&[".vtuber.v1"])?;

    Ok(())
}
