from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerationRequest(_message.Message):
    __slots__ = ("persona_id", "overrides")
    PERSONA_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    persona_id: str
    overrides: PersonaOverrides
    def __init__(self, persona_id: _Optional[str] = ..., overrides: _Optional[_Union[PersonaOverrides, _Mapping]] = ...) -> None: ...

class PersonaOverrides(_message.Message):
    __slots__ = ("hair_style", "eye_color", "outfit")
    HAIR_STYLE_FIELD_NUMBER: _ClassVar[int]
    EYE_COLOR_FIELD_NUMBER: _ClassVar[int]
    OUTFIT_FIELD_NUMBER: _ClassVar[int]
    hair_style: str
    eye_color: str
    outfit: str
    def __init__(self, hair_style: _Optional[str] = ..., eye_color: _Optional[str] = ..., outfit: _Optional[str] = ...) -> None: ...

class GenerationResponse(_message.Message):
    __slots__ = ("image_url", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, image_url: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
