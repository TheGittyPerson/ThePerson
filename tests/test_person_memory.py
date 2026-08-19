"""Pytest coverage for Person memory methods (remember, recall, forget)."""

import pytest

from theperson.person import Person


def test_memory_initial_state() -> None:
    person = Person()
    assert person.recall() is None


def test_remember_and_recall() -> None:
    person = Person()
    person.remember("Buy groceries")
    assert person.recall() == "Buy groceries"


def test_recall_with_say(capsys: pytest.CaptureFixture[str]) -> None:
    person = Person()
    person.remember("Buy groceries")
    recalled = person.recall(say=True)
    captured = capsys.readouterr()
    assert recalled == "Buy groceries"
    assert captured.out == "Buy groceries\n"


def test_recall_with_say_when_empty(capsys: pytest.CaptureFixture[str]) -> None:
    person = Person()
    recalled = person.recall(say=True)
    captured = capsys.readouterr()
    assert recalled is None
    assert captured.out == ""


def test_forget() -> None:
    person = Person()
    person.remember("Buy groceries")
    assert person.recall() == "Buy groceries"
    person.forget()
    assert person.recall() is None


def test_remember_type_error() -> None:
    person = Person()
    with pytest.raises(TypeError):
        person.remember(123)  # type: ignore[arg-type]


def test_recall_type_error() -> None:
    person = Person()
    with pytest.raises(TypeError):
        person.recall(say="True")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        person.recall(say=1)  # type: ignore[arg-type]
