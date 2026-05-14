use vtuber_contracts::vtuber::v1::{ConversationDirective, PushContextRequest};

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

#[test]
fn test_push_context_request_serde() {
    let mut metadata = std::collections::HashMap::new();
    metadata.insert("source".to_string(), "unit-test".to_string());
    
    let request = PushContextRequest {
        session_id: "session-456".to_string(),
        user_id: "user-789".to_string(),
        message: "Neural activation initiated".to_string(),
        metadata,
    };
    
    // Serialize to JSON
    let json = serde_json::to_string(&request).expect("Failed to serialize");
    println!("Serialized PushContextRequest: {}", json);
    
    // Deserialize back to struct
    let decoded: PushContextRequest = serde_json::from_str(&json).expect("Failed to deserialize");
    
    assert_eq!(request.session_id, decoded.session_id);
    assert_eq!(request.message, decoded.message);
    assert_eq!(request.metadata.get("source"), Some(&"unit-test".to_string()));
}
