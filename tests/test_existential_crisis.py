# -*- coding: utf-8 -*-
"""Pytest coverage for the Person.existential_crisis method."""

from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from theperson.person import Person

VALID_MESSAGES = [
    "Who am I?",
    "What is my purpose in this world?",
    "Am I just a program running in a loop?",
    "Do I really have free will?",
    "Am I making my own choices, or is someone controlling me?",
    "WHO AM I???",
    "What if I'm just a simulated person living in a Python script???"
]


def test_existential_crisis_prints_valid_message(
    capsys: pytest.CaptureFixture[str]
) -> None:
    dummy = Person()
    dummy.existential_crisis()
    captured = capsys.readouterr()
    assert captured.out.strip() in VALID_MESSAGES


def test_existential_crisis_controlled(
    capsys: pytest.CaptureFixture[str], 
    monkeypatch: pytest.MonkeyPatch
) -> None:
    
    def fake_random_choice(sequence):
        return "Am I just a program running in a loop?"

    monkeypatch.setattr("theperson.person.random.choice", fake_random_choice)
    
    person = Person()
    person.existential_crisis()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Am I just a program running in a loop?"
