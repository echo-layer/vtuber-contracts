from google.protobuf import timestamp_pb2 as _timestamp_pb2
from vtuber.v1 import persona_pb2 as _persona_pb2
from vtuber.v1 import voice_profile_pb2 as _voice_profile_pb2
from vtuber.v1 import tool_call_pb2 as _tool_call_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationDirective(_message.Message):
    __slots__ = ("directive_id", "emitted_at", "persona_id", "text_prompt", "voice_prompt", "emotion", "target_audio_format", "max_latency_ms", "tool_calls")
    DIRECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
    EMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    PERSONA_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    VOICE_PROMPT_FIELD_NUMBER: _ClassVar[int]
    EMOTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    directive_id: str
    emitted_at: _timestamp_pb2.Timestamp
    persona_id: _persona_pb2.PersonaId
    text_prompt: str
    voice_prompt: str
    emotion: _voice_profile_pb2.Emotion
    target_audio_format: _voice_profile_pb2.AudioFormat
    max_latency_ms: int
    tool_calls: _containers.RepeatedCompositeFieldContainer[_tool_call_pb2.ToolCall]
    def __init__(self, directive_id: _Optional[str] = ..., emitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., persona_id: _Optional[_Union[_persona_pb2.PersonaId, str]] = ..., text_prompt: _Optional[str] = ..., voice_prompt: _Optional[str] = ..., emotion: _Optional[_Union[_voice_profile_pb2.Emotion, str]] = ..., target_audio_format: _Optional[_Union[_voice_profile_pb2.AudioFormat, str]] = ..., max_latency_ms: _Optional[int] = ..., tool_calls: _Optional[_Iterable[_Union[_tool_call_pb2.ToolCall, _Mapping]]] = ...) -> None: ...

class DirectiveAck(_message.Message):
    __slots__ = ("directive_id", "accepted", "reject_reason")
    DIRECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECT_REASON_FIELD_NUMBER: _ClassVar[int]
    directive_id: str
    accepted: bool
    reject_reason: str
    def __init__(self, directive_id: _Optional[str] = ..., accepted: bool = ..., reject_reason: _Optional[str] = ...) -> None: ...

class EmitDirectiveRequest(_message.Message):
    __slots__ = ("directive",)
    DIRECTIVE_FIELD_NUMBER: _ClassVar[int]
    directive: ConversationDirective
    def __init__(self, directive: _Optional[_Union[ConversationDirective, _Mapping]] = ...) -> None: ...

class EmitDirectiveResponse(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: DirectiveAck
    def __init__(self, ack: _Optional[_Union[DirectiveAck, _Mapping]] = ...) -> None: ...
