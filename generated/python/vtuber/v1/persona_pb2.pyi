from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonaId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERSONA_ID_UNSPECIFIED: _ClassVar[PersonaId]
    PERSONA_ID_VALORA: _ClassVar[PersonaId]
    PERSONA_ID_AURORA: _ClassVar[PersonaId]
    PERSONA_ID_AMETRA: _ClassVar[PersonaId]
    PERSONA_ID_ASTRAEA: _ClassVar[PersonaId]
    PERSONA_ID_ELDORA: _ClassVar[PersonaId]
PERSONA_ID_UNSPECIFIED: PersonaId
PERSONA_ID_VALORA: PersonaId
PERSONA_ID_AURORA: PersonaId
PERSONA_ID_AMETRA: PersonaId
PERSONA_ID_ASTRAEA: PersonaId
PERSONA_ID_ELDORA: PersonaId

class Persona(_message.Message):
    __slots__ = ("id", "display_name", "description", "activation_keywords", "lore_tags", "color_hex")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    LORE_TAGS_FIELD_NUMBER: _ClassVar[int]
    COLOR_HEX_FIELD_NUMBER: _ClassVar[int]
    id: PersonaId
    display_name: str
    description: str
    activation_keywords: _containers.RepeatedScalarFieldContainer[str]
    lore_tags: _containers.RepeatedScalarFieldContainer[str]
    color_hex: str
    def __init__(self, id: _Optional[_Union[PersonaId, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., activation_keywords: _Optional[_Iterable[str]] = ..., lore_tags: _Optional[_Iterable[str]] = ..., color_hex: _Optional[str] = ...) -> None: ...
