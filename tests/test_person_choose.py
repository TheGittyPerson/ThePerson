from pathlib import Path
import sys
import os
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from unittest.mock import Mock
from typing import Sequence, Any
from theperson.person import Person


@pytest.fixture(params=[
    ["apple", "banana", "cherry"],
    [1, 2, 3, 4],
    ["foo", 42, True],
    (10, 20, 30),
])

def sample_iterable(request) -> Sequence[Any]:
    """Fixture for providing various non-empty iterables."""
    return request.param


@pytest.fixture(params=[[], (), ""])
def empty_iterable(request):
    """Fixture for empty iterables."""
    return request.param


@pytest.fixture
def mock_random(monkeypatch: pytest.MonkeyPatch):
    """Mock random.choice to always return the first element."""
    def mock_choice(iterable: Sequence[Any]) -> Any:
        return iterable[0]
    
    monkeypatch.setattr("random.choice", mock_choice)


def test_choose_non_empty(mock_random, sample_iterable):
    """Test Person.choose on non-empty iterables (mocked random, returns first)."""
    result = Person.choose(sample_iterable)
    assert result == sample_iterable[0]
    assert result in sample_iterable


def test_choose_empty_raises_IndexError(empty_iterable):
    """Test Person.choose raises IndexError on empty iterable."""
    with pytest.raises(IndexError):
        Person.choose(empty_iterable)
