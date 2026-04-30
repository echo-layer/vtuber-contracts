//! Persona YAML round-trip test — the coupling gate with vtuber-commons.
//!
//! vtuber-commons loads one YAML per persona and validates it against the
//! Persona proto. If this test fails, the YAML shape in
//! `samples/personas/*.yaml` has drifted from the proto schema and commons
//! will block at startup once it wires up. Keep them in lockstep.

use serde::{Deserialize, Serialize};
use vtuber_contracts::vtuber::v1::{Persona, PersonaId};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct PersonaYaml {
    id: String,
    display_name: String,
    description: String,
    activation_keywords: Vec<String>,
    lore_tags: Vec<String>,
    color_hex: String,
}

impl PersonaYaml {
    fn to_proto(&self) -> Persona {
        let id = match self.id.as_str() {
            "PERSONA_ID_VALORA" => PersonaId::Valora,
            "PERSONA_ID_AURORA" => PersonaId::Aurora,
            "PERSONA_ID_AMETRA" => PersonaId::Ametra,
            "PERSONA_ID_ASTRAEA" => PersonaId::Astraea,
            "PERSONA_ID_ELDORA" => PersonaId::Eldora,
            _ => PersonaId::Unspecified,
        };
        Persona {
            id: id as i32,
            display_name: self.display_name.clone(),
            description: self.description.clone(),
            activation_keywords: self.activation_keywords.clone(),
            lore_tags: self.lore_tags.clone(),
            color_hex: self.color_hex.clone(),
        }
    }
}

#[test]
fn valora_yaml_loads_to_valid_proto() {
    let yaml = std::fs::read_to_string("samples/personas/valora.yaml").unwrap();
    let parsed: PersonaYaml = serde_yaml::from_str(&yaml).unwrap();
    let proto = parsed.to_proto();

    assert_eq!(proto.id(), PersonaId::Valora);
    assert_eq!(proto.display_name, "Valora");
    assert!(!proto.activation_keywords.is_empty());
    assert!(proto.color_hex.starts_with('#'));
    assert_eq!(proto.color_hex.len(), 7);
}

#[test]
fn aurora_yaml_loads_to_valid_proto() {
    let yaml = std::fs::read_to_string("samples/personas/aurora.yaml").unwrap();
    let parsed: PersonaYaml = serde_yaml::from_str(&yaml).unwrap();
    let proto = parsed.to_proto();

    assert_eq!(proto.id(), PersonaId::Aurora);
    assert_eq!(proto.display_name, "Aurora");
}

#[test]
fn no_persona_yaml_maps_to_unspecified() {
    // Guard: every sample YAML MUST resolve to a real persona. A mapping
    // to PERSONA_ID_UNSPECIFIED means the id string in the YAML does not
    // match any known variant — catch that at test time, not runtime.
    for entry in std::fs::read_dir("samples/personas").unwrap() {
        let path = entry.unwrap().path();
        if path.extension().and_then(|s| s.to_str()) != Some("yaml") {
            continue;
        }
        let yaml = std::fs::read_to_string(&path).unwrap();
        let parsed: PersonaYaml = serde_yaml::from_str(&yaml).unwrap();
        let proto = parsed.to_proto();
        assert_ne!(
            proto.id(),
            PersonaId::Unspecified,
            "{} resolved to UNSPECIFIED — check the `id` field",
            path.display()
        );
    }
}
