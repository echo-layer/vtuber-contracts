use vtuber_contracts::vtuber::v1::ConversationDirective;

#[test]
fn test_directive_serde_json() {
    let directive = ConversationDirective {
        directive_id: "test-123".to_string(),
        text_prompt: "Hello".to_string(),
        ..Default::default()
    };
    
    // Serialize to JSON
    let json = serde_json::to_string(&directive).expect("Failed to serialize");
    println!("Serialized JSON: {}", json);
    
    // Deserialize back to struct
    let decoded: ConversationDirective = serde_json::from_str(&json).expect("Failed to deserialize");
    
    assert_eq!(directive.directive_id, decoded.directive_id);
    assert_eq!(directive.text_prompt, decoded.text_prompt);
}
