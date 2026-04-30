"""Mojo bindings for vtuber-contracts.

Mojo has no native proto3 codegen as of Modular's 2026 tooling. This module
wraps the Python bindings that `buf generate` produces under
`generated/python/vtuber/v1/*_pb2.py` via Mojo's Python interop. See
ADR-004 in DESIGN_DECISIONS.md.

Every struct here is a thin Mojo facade over a held `PythonObject`. The
on-the-wire shape is defined exclusively by proto/vtuber/v1/*.proto — if
the Python module is missing the shape, this file will not compile when
the round-trip test runs, which is the intended failure mode.
"""

from std.python import Python, PythonObject


def _persona_module() raises -> PythonObject:
    return Python.import_module("vtuber.v1.persona_pb2")


def _voice_profile_module() raises -> PythonObject:
    return Python.import_module("vtuber.v1.voice_profile_pb2")


def _conversation_module() raises -> PythonObject:
    return Python.import_module("vtuber.v1.conversation_pb2")


struct Persona:
    """Mojo view over a vtuber.v1.Persona proto instance."""

    var _py: PythonObject

    def __init__(out self, py: PythonObject):
        self._py = py

    @staticmethod
    def new(
        persona_id: Int,
        display_name: String,
        description: String,
        color_hex: String,
    ) raises -> Persona:
        var pb = _persona_module()
        var obj = pb.Persona()
        obj.id = persona_id
        obj.display_name = display_name
        obj.description = description
        obj.color_hex = color_hex
        return Persona(obj)

    def serialize(self) raises -> PythonObject:
        return self._py.SerializeToString()

    @staticmethod
    def parse(data: PythonObject) raises -> Persona:
        var pb = _persona_module()
        var obj = pb.Persona()
        obj.ParseFromString(data)
        return Persona(obj)

    def display_name(self) raises -> String:
        return String(self._py.display_name)

    def color_hex(self) raises -> String:
        return String(self._py.color_hex)


struct ConversationDirective:
    """Mojo view over a vtuber.v1.ConversationDirective proto instance."""

    var _py: PythonObject

    def __init__(out self, py: PythonObject):
        self._py = py

    @staticmethod
    def new(
        directive_id: String,
        persona_id: Int,
        text_prompt: String,
        voice_prompt: String = "",
        emotion: Int = 1, # EMOTION_NEUTRAL
        target_audio_format: Int = 1, # AUDIO_FORMAT_WAV
        max_latency_ms: Int = 0,
    ) raises -> ConversationDirective:
        var pb = _conversation_module()
        var obj = pb.ConversationDirective()
        obj.directive_id = directive_id
        obj.persona_id = persona_id
        obj.text_prompt = text_prompt
        obj.voice_prompt = voice_prompt
        obj.emotion = emotion
        obj.target_audio_format = target_audio_format
        obj.max_latency_ms = max_latency_ms
        return ConversationDirective(obj)

    def serialize(self) raises -> PythonObject:
        return self._py.SerializeToString()

    @staticmethod
    def parse(data: PythonObject) raises -> ConversationDirective:
        var pb = _conversation_module()
        var obj = pb.ConversationDirective()
        obj.ParseFromString(data)
        return ConversationDirective(obj)

    def directive_id(self) raises -> String:
        return String(self._py.directive_id)

    def persona_id(self) raises -> PythonObject:
        return self._py.persona_id

    def text_prompt(self) raises -> String:
        return String(self._py.text_prompt)

    def voice_prompt(self) raises -> String:
        return String(self._py.voice_prompt)

    def emotion(self) raises -> PythonObject:
        return self._py.emotion

    def target_audio_format(self) raises -> PythonObject:
        return self._py.target_audio_format

    def max_latency_ms(self) raises -> PythonObject:
        return self._py.max_latency_ms
