from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonaAssetSchema(_message.Message):
    __slots__ = ("identity", "personality", "assets", "metadata")
    class Identity(_message.Message):
        __slots__ = ("id", "name", "version", "description")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        version: str
        description: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class Personality(_message.Message):
        __slots__ = ("traits", "language", "tone")
        TRAITS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        TONE_FIELD_NUMBER: _ClassVar[int]
        traits: _containers.RepeatedScalarFieldContainer[str]
        language: str
        tone: str
        def __init__(self, traits: _Optional[_Iterable[str]] = ..., language: _Optional[str] = ..., tone: _Optional[str] = ...) -> None: ...
    class Assets(_message.Message):
        __slots__ = ("voice_profile_id", "avatar_id")
        VOICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
        AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
        voice_profile_id: str
        avatar_id: str
        def __init__(self, voice_profile_id: _Optional[str] = ..., avatar_id: _Optional[str] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("created_at", "updated_at", "tags")
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        updated_at: _timestamp_pb2.Timestamp
        tags: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    identity: PersonaAssetSchema.Identity
    personality: PersonaAssetSchema.Personality
    assets: PersonaAssetSchema.Assets
    metadata: PersonaAssetSchema.Metadata
    def __init__(self, identity: _Optional[_Union[PersonaAssetSchema.Identity, _Mapping]] = ..., personality: _Optional[_Union[PersonaAssetSchema.Personality, _Mapping]] = ..., assets: _Optional[_Union[PersonaAssetSchema.Assets, _Mapping]] = ..., metadata: _Optional[_Union[PersonaAssetSchema.Metadata, _Mapping]] = ...) -> None: ...

class VoiceProfileSchema(_message.Message):
    __slots__ = ("id", "name", "provider", "voice_id", "settings", "metadata")
    class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVIDER_UNSPECIFIED: _ClassVar[VoiceProfileSchema.Provider]
        PROVIDER_ELEVENLABS: _ClassVar[VoiceProfileSchema.Provider]
        PROVIDER_AZURE: _ClassVar[VoiceProfileSchema.Provider]
        PROVIDER_OPENAI: _ClassVar[VoiceProfileSchema.Provider]
        PROVIDER_COQUI: _ClassVar[VoiceProfileSchema.Provider]
    PROVIDER_UNSPECIFIED: VoiceProfileSchema.Provider
    PROVIDER_ELEVENLABS: VoiceProfileSchema.Provider
    PROVIDER_AZURE: VoiceProfileSchema.Provider
    PROVIDER_OPENAI: VoiceProfileSchema.Provider
    PROVIDER_COQUI: VoiceProfileSchema.Provider
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    provider: VoiceProfileSchema.Provider
    voice_id: str
    settings: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[_Union[VoiceProfileSchema.Provider, str]] = ..., voice_id: _Optional[str] = ..., settings: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ModelRegistrySchema(_message.Message):
    __slots__ = ("llm_models", "allowed_models")
    class LLMModel(_message.Message):
        __slots__ = ("id", "provider", "max_tokens", "temperature")
        ID_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        id: str
        provider: str
        max_tokens: int
        temperature: float
        def __init__(self, id: _Optional[str] = ..., provider: _Optional[str] = ..., max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ...) -> None: ...
    class AllowedModel(_message.Message):
        __slots__ = ("id", "type", "version")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[ModelRegistrySchema.AllowedModel.Type]
            TYPE_CHECKPOINT: _ClassVar[ModelRegistrySchema.AllowedModel.Type]
            TYPE_LORA: _ClassVar[ModelRegistrySchema.AllowedModel.Type]
            TYPE_EMBEDDING: _ClassVar[ModelRegistrySchema.AllowedModel.Type]
        TYPE_UNSPECIFIED: ModelRegistrySchema.AllowedModel.Type
        TYPE_CHECKPOINT: ModelRegistrySchema.AllowedModel.Type
        TYPE_LORA: ModelRegistrySchema.AllowedModel.Type
        TYPE_EMBEDDING: ModelRegistrySchema.AllowedModel.Type
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: ModelRegistrySchema.AllowedModel.Type
        version: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[ModelRegistrySchema.AllowedModel.Type, str]] = ..., version: _Optional[str] = ...) -> None: ...
    LLM_MODELS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODELS_FIELD_NUMBER: _ClassVar[int]
    llm_models: _containers.RepeatedCompositeFieldContainer[ModelRegistrySchema.LLMModel]
    allowed_models: _containers.RepeatedCompositeFieldContainer[ModelRegistrySchema.AllowedModel]
    def __init__(self, llm_models: _Optional[_Iterable[_Union[ModelRegistrySchema.LLMModel, _Mapping]]] = ..., allowed_models: _Optional[_Iterable[_Union[ModelRegistrySchema.AllowedModel, _Mapping]]] = ...) -> None: ...
