"""Tests for the hp attribute in the Physical dataclass and Person class."""

from theperson.person import Person, Physical


def test_physical_hp_default_none() -> None:
    physical = Physical()
    assert physical.hp is None


def test_physical_hp_initialization() -> None:
    physical = Physical(hp=100)
    assert physical.hp == 100


def test_person_physical_hp() -> None:
    person = Person(physical=Physical(hp=75))
    assert person.physical.hp == 75

    person.physical.hp -= 25
    assert person.physical.hp == 50
