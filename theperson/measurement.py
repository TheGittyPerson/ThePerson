"""Module containing the Measurement class for storing a value with a unit."""

from __future__ import annotations

from functools import total_ordering
from math import isclose

# Base conversion factors to metres
_TO_METRES: dict[str, float] = {
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "ft": 0.3048,
    "in": 0.0254,
}

VALID_UNITS = {
    "m": "metres",
    "cm": "centimetres",
    "mm": "millimetres",
    "ft": "feet",
    "in": "inches",
}

_UNIT_ERROR_HINT = (
    "Valid short forms: m, cm, mm, ft, in "
    "(metres, centimetres, millimetres, feet, inches)."
)


@total_ordering
class Measurement:
    """A class to represent a measurement with a value and unit.

    Attributes:
        value: The numeric value of the measurement.
        unit: The unit of the measurement (e.g. 'm', 'cm', 'ft').
    """

    def __init__(self, value: float, unit: str = "m") -> None:
        """Initialise the measurement.

        Args:
            value: The numeric value of the measurement.
            unit: The unit of measurement. Defaults to 'm'.

        Raises:
            TypeError: If value is not a number or unit is not a string.
            ValueError: If value is negative or unit is not recognised.
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"Value must be a number, got {type(value).__name__}."
            )
        if value < 0:
            raise ValueError("Value must be non-negative.")
        if not isinstance(unit, str):
            raise TypeError(
                f"Unit must be a string, got {type(unit).__name__}."
            )
        unit = unit.lower().strip()
        if unit not in VALID_UNITS:
            raise ValueError(
                f"'{unit}' is not a recognised unit. "
                f"{_UNIT_ERROR_HINT}"
            )
        self.value = float(value)
        self.unit = unit

    def to_metres(self) -> float:
        """Convert the measurement to metres.

        Returns:
            The value in metres as a float.
        """
        return self.value * _TO_METRES[self.unit]

    def to_unit(self, unit: str) -> "Measurement":
        """Convert the measurement to another unit.

        Args:
            unit: The target unit to convert to.

        Returns:
            A new Measurement in the target unit.

        Raises:
            TypeError: If unit is not a string.
            ValueError: If unit is not recognised.
        """
        if not isinstance(unit, str):
            raise TypeError(
                f"Unit must be a string, got {type(unit).__name__}."
            )
        unit = unit.lower().strip()
        if unit not in VALID_UNITS:
            raise ValueError(
                f"'{unit}' is not a recognised unit. "
                f"{_UNIT_ERROR_HINT}"
            )
        metres = self.to_metres()
        return Measurement(metres / _TO_METRES[unit], unit)

    def describe(self, precision: int = 2) -> str:
        """Return a human-readable description of the measurement.

        Args:
            precision: Number of decimal places. Defaults to 2.

        Returns:
            A string describing the measurement.
        """
        return f"{self.value:.{precision}f} {VALID_UNITS[self.unit]}"

    def __str__(self) -> str:
        """Return a string representation with full precision."""
        return f"{self.value} {VALID_UNITS[self.unit]}"

    def __repr__(self) -> str:
        """Return a detailed representation of the measurement."""
        return f"Measurement(value={self.value}, unit={self.unit!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality by comparing values in metres with tolerance."""
        if not isinstance(other, Measurement):
            return NotImplemented
        return isclose(self.to_metres(), other.to_metres(), abs_tol=1e-9)

    def __lt__(self, other: object) -> bool:
        """Check if this measurement is less than another."""
        if not isinstance(other, Measurement):
            return NotImplemented
        return self.to_metres() < other.to_metres()