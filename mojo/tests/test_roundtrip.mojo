"""Mojo round-trip tests — coupling gate with the Python-generated stubs.

These tests fail loudly if the Python bindings under generated/python/ are
missing, out of date, or shaped differently from the Mojo facade. Run via
`pixi run test`, which sets PYTHONPATH=generated/python so the import
resolves without a Python package install step.
"""

from std.testing import assert_equal
from vtuber_contracts import Persona, ConversationDirective


def test_persona_roundtrip() raises:
    var valora_id = 1  # PersonaId.PERSONA_ID_VALORA
    var original = Persona.new(
        valora_id,
        "Valora",
        "Russian accent, dark humor.",
        "#FF3C3C",
    )
    var bytes = original.serialize()
    var decoded = Persona.parse(bytes)
    assert_equal(decoded.display_name(), "Valora")
    assert_equal(decoded.color_hex(), "#FF3C3C")


def test_conversation_directive_roundtrip() raises:
    var ametra_id = 3  # PersonaId.PERSONA_ID_AMETRA
    # Using full arguments to avoid Mojo 24.x interop issues with defaults
    var original = ConversationDirective.new(
        "018f4e2b-4a8c-7b1f-9c5e-2d3a4b5c6d7e",
        ametra_id,
        "สวัสดี ยินดีที่ได้รู้จัก!",  # Thai Unicode verification
        "",  # voice_prompt
        1,  # emotion neutral
        1,  # audio format wav
        500,  # latency
    )
    var bytes = original.serialize()
    var decoded = ConversationDirective.parse(bytes)
    assert_equal(
        decoded.text_prompt(),
        "สวัสดี ยินดีที่ได้รู้จัก!",
    )
    assert_equal(String(decoded.max_latency_ms()), "500")


def main() raises:
    test_persona_roundtrip()
    test_conversation_directive_roundtrip()
    print("Mojo roundtrip tests: OK")
