fn main() -> Result<(), Box<dyn std::error::Error>> {
    let protos = &[
        "proto/vtuber/v1/persona.proto",
        "proto/vtuber/v1/voice_profile.proto",
        "proto/vtuber/v1/conversation.proto",
    ];

    for p in protos {
        println!("cargo:rerun-if-changed={p}");
    }
    println!("cargo:rerun-if-changed=build.rs");

    tonic_build::configure()
        .build_server(true)
        .build_client(true)
        .compile_protos(protos, &["proto"])?;

    Ok(())
}
