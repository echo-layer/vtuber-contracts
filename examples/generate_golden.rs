use prost::Message;
use std::fs::File;
use std::io::Write;
use std::time::SystemTime;
use vtuber_contracts::vtuber::v1::{AudioFormat, ConversationDirective, Emotion, PersonaId};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let now = SystemTime::now().duration_since(SystemTime::UNIX_EPOCH)?;

    let directive = ConversationDirective {
        directive_id: "test-golden-roundtrip-001".to_string(),
        emitted_at: Some(prost_types::Timestamp {
            seconds: now.as_secs() as i64,
            nanos: now.subsec_nanos() as i32,
        }),
        persona_id: PersonaId::Valora as i32,
        text_prompt: "สวัสดี ยินดีที่ได้รู้จัก!".to_string(),
        voice_prompt: "thai-accent-test".to_string(),
        emotion: Emotion::Happy as i32,
        target_audio_format: AudioFormat::Wav as i32,
        max_latency_ms: 500,
    };

    let mut buf = Vec::new();
    directive.encode(&mut buf)?;

    let mut file = File::create("golden_directive.bin")?;
    file.write_all(&buf)?;

    println!("Successfully generated golden_directive.bin from Rust");
    Ok(())
}
