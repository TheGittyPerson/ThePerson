from pathlib import Path
import sys
import pytest
from typing import Sequence, Any
from theperson.person import Person

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


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


def test_choose_non_empty(sample_iterable):
    """Test Person.choose on non-empty iterables."""

    result = Person.choose(sample_iterable)
    assert result in sample_iterable


def test_choose_empty_raises_indexerror(empty_iterable):
    """Test Person.choose raises IndexError on empty iterable."""

    with pytest.raises(IndexError):
        Person.choose(empty_iterable)
