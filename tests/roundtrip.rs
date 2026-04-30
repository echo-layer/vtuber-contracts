//! Round-trip serialization tests for the three v0.1 messages.
//!
//! These lock the wire shape in place so any accidental field renumbering
//! or proto-level breaking change shows up as a Rust test failure in
//! addition to the `buf breaking` gate (ADR-003).

use prost::Message;
use vtuber_contracts::vtuber::v1::{
    AudioFormat, ConversationDirective, DirectiveAck, Emotion, Persona, PersonaId, VoiceProfile,
};

#[test]
fn persona_roundtrip() {
    let original = Persona {
        id: PersonaId::Valora as i32,
        display_name: "Valora".into(),
        description: "Russian accent, dark humor, chaos trigger.".into(),
        activation_keywords: vec!["chaos".into(), "meme".into(), "dark".into()],
        lore_tags: vec!["russian-accent".into(), "edgy".into(), "red".into()],
        color_hex: "#FF3C3C".into(),
    };
    let decoded = Persona::decode(original.encode_to_vec().as_slice()).unwrap();
    assert_eq!(original, decoded);
    assert_eq!(decoded.id(), PersonaId::Valora);
}

#[test]
fn voice_profile_roundtrip() {
    let original = VoiceProfile {
        persona_id: PersonaId::Aurora as i32,
        base_pitch: 0.12,
        speaking_rate: 0.9,
        energy: 0.35,
        style_tag: "asmr".into(),
        accent_hint: "soft-american".into(),
        quirks: vec!["ehehe".into(), "mm-hmm".into()],
    };
    let decoded = VoiceProfile::decode(original.encode_to_vec().as_slice()).unwrap();
    assert_eq!(original, decoded);
}

#[test]
fn conversation_directive_roundtrip() {
    let original = ConversationDirective {
        directive_id: "018f4e2b-4a8c-7b1f-9c5e-2d3a4b5c6d7e".into(),
        emitted_at: Some(prost_types::Timestamp {
            seconds: 1_713_792_000,
            nanos: 0,
        }),
        persona_id: PersonaId::Ametra as i32,
        text_prompt: "Let me analyze that for a moment...".into(),
        voice_prompt: "thoughtful, philosophical".into(),
        emotion: Emotion::Analytical as i32,
        target_audio_format: AudioFormat::Opus as i32,
        max_latency_ms: 800,
        tool_calls: vec![],
    };
    let decoded = ConversationDirective::decode(original.encode_to_vec().as_slice()).unwrap();
    assert_eq!(original, decoded);
}

#[test]
fn directive_ack_reject_reason_is_stable() {
    // The reject_reason field is a stable short code, not a human-readable
    // string. Downstream consumers branch on the code value — tests pin the
    // expected codes so they do not drift.
    for code in [
        "persona_unknown",
        "format_unsupported",
        "queue_full",
        "voice_profile_missing",
    ] {
        let ack = DirectiveAck {
            directive_id: "test".into(),
            accepted: false,
            reject_reason: code.into(),
        };
        let decoded = DirectiveAck::decode(ack.encode_to_vec().as_slice()).unwrap();
        assert_eq!(decoded.reject_reason, code);
    }
}
