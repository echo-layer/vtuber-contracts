from vtuber.v1 import persona_pb2 as _persona_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_FORMAT_UNSPECIFIED: _ClassVar[AudioFormat]
    AUDIO_FORMAT_WAV: _ClassVar[AudioFormat]
    AUDIO_FORMAT_OPUS: _ClassVar[AudioFormat]
    AUDIO_FORMAT_MP3: _ClassVar[AudioFormat]

class Emotion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMOTION_UNSPECIFIED: _ClassVar[Emotion]
    EMOTION_NEUTRAL: _ClassVar[Emotion]
    EMOTION_HAPPY: _ClassVar[Emotion]
    EMOTION_SAD: _ClassVar[Emotion]
    EMOTION_ANGRY: _ClassVar[Emotion]
    EMOTION_PLAYFUL: _ClassVar[Emotion]
    EMOTION_ANALYTICAL: _ClassVar[Emotion]
    EMOTION_ASMR_CALM: _ClassVar[Emotion]
AUDIO_FORMAT_UNSPECIFIED: AudioFormat
AUDIO_FORMAT_WAV: AudioFormat
AUDIO_FORMAT_OPUS: AudioFormat
AUDIO_FORMAT_MP3: AudioFormat
EMOTION_UNSPECIFIED: Emotion
EMOTION_NEUTRAL: Emotion
EMOTION_HAPPY: Emotion
EMOTION_SAD: Emotion
EMOTION_ANGRY: Emotion
EMOTION_PLAYFUL: Emotion
EMOTION_ANALYTICAL: Emotion
EMOTION_ASMR_CALM: Emotion

class VoiceProfile(_message.Message):
    __slots__ = ("persona_id", "base_pitch", "speaking_rate", "energy", "style_tag", "accent_hint", "quirks")
    PERSONA_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_PITCH_FIELD_NUMBER: _ClassVar[int]
    SPEAKING_RATE_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    STYLE_TAG_FIELD_NUMBER: _ClassVar[int]
    ACCENT_HINT_FIELD_NUMBER: _ClassVar[int]
    QUIRKS_FIELD_NUMBER: _ClassVar[int]
    persona_id: _persona_pb2.PersonaId
    base_pitch: float
    speaking_rate: float
    energy: float
    style_tag: str
    accent_hint: str
    quirks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, persona_id: _Optional[_Union[_persona_pb2.PersonaId, str]] = ..., base_pitch: _Optional[float] = ..., speaking_rate: _Optional[float] = ..., energy: _Optional[float] = ..., style_tag: _Optional[str] = ..., accent_hint: _Optional[str] = ..., quirks: _Optional[_Iterable[str]] = ...) -> None: ...
