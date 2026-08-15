"""Unit tests for Person.birth() method."""

from datetime import date
from theperson.person import Person, Profile


def test_person_birth_basic() -> None:
    parent = Person(profile=Profile(name="Alice", age=28, nationality="Romanian"))
    baby = parent.birth(baby_name="Leo", gender="male")

    assert isinstance(baby, Person)
    assert baby.profile.name == "Leo"
    assert baby.profile.age == 0
    assert baby.profile.gender == "male"
    assert baby.profile.nationality == "Romanian"
    assert baby.life_dates.birthday_date == date.today()
    assert parent.mood.name == "excited"
    assert baby.mood.name == "happy"


def test_person_birth_unnamed() -> None:
    parent = Person(profile=Profile(name="Elena", age=30))
    baby = parent.birth()

    assert baby.profile.name is None
    assert baby.profile.age == 0
    assert baby.physical.height == 0.5
    assert baby.physical.weight == 3.5
