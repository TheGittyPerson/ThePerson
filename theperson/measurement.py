"""Measurement module for storing a value with a unit."""

from __future__ import annotations

from math import isclose


class Measurement:
    """A class to represent a measurement with a numeric value and unit.

    Attributes:
        value: The numeric measurement value.
        unit: The canonical unit name for the measurement.
    """

    UNIT_ALIASES: dict[str, str] = {
        "m": "meters",
        "meter": "meters",
        "meters": "meters",
        "cm": "centimeters",
        "centimeter": "centimeters",
        "centimeters": "centimeters",
        "mm": "millimeters",
        "millimeter": "millimeters",
        "millimeters": "millimeters",
        "ft": "feet",
        "foot": "feet",
        "feet": "feet",
        "in": "inches",
        "inch": "inches",
        "inches": "inches",
    }
    CONVERSION_TO_METERS: dict[str, float] = {
        "meters": 1.0,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "feet": 0.3048,
        "inches": 0.0254,
    }
    VALID_UNITS: tuple[str, ...] = tuple(CONVERSION_TO_METERS)

    def __init__(self, value: float, unit: str = "meters") -> None:
        """Initialize the measurement.

        Args:
            value: The numeric value of the measurement. Must be non-negative.
            unit: The unit of the measurement. Defaults to 'meters'.

        Raises:
            TypeError: If value is not numeric or unit is not a string.
            ValueError: If value is negative or unit is not recognized.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Measurement value must be numeric, got {type(value).__name__}"
            )
        if not isinstance(unit, str):
            raise TypeError(
                f"Measurement unit must be a string, got {type(unit).__name__}"
            )

        normalized_unit = self._normalize_unit(unit)
        numeric_value = float(value)
        if numeric_value < 0:
            raise ValueError(
                f"Measurement value must be non-negative, got {value}"
            )

        self.value = numeric_value
        self.unit = normalized_unit

    @classmethod
    def _normalize_unit(cls, unit: str) -> str:
        normalized = unit.strip().lower()
        if normalized not in cls.UNIT_ALIASES:
            raise ValueError(
                f"Unit '{unit}' is not recognized. "
                f"Valid units are: {', '.join(cls.VALID_UNITS)}"
            )
        return cls.UNIT_ALIASES[normalized]

    @staticmethod
    def _format_value(value: float) -> str:
        return f"{value:g}"

    def to_meters(self) -> float:
        """Return the measurement converted to meters."""
        return self.value * self.CONVERSION_TO_METERS[self.unit]

    def to_unit(self, unit: str) -> "Measurement":
        """Return a converted measurement in the requested unit."""
        normalized_unit = self._normalize_unit(unit)
        converted_value = (
            self.to_meters() / self.CONVERSION_TO_METERS[normalized_unit]
        )
        return Measurement(converted_value, normalized_unit)

    def describe(self, precision: int = 2) -> str:
        """Return a human-readable string representation."""
        if precision < 0:
            raise ValueError(f"Precision must be non-negative, got {precision}")
        rounded_value = round(self.value, precision)
        return f"{rounded_value:g} {self.unit}"

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return (
            f"Measurement(value={self._format_value(self.value)}, "
            f"unit={self.unit!r})"
        )

    def __str__(self) -> str:
        """Return a human-readable string of the measurement."""
        return self.describe()

    def __eq__(self, other: object) -> bool:
        """Compare measurements by their value in meters."""
        if not isinstance(other, Measurement):
            return NotImplemented
        return isclose(self.to_meters(), other.to_meters(), rel_tol=0.0,
                       abs_tol=1e-9)

    def __lt__(self, other: object) -> bool:
        """Compare whether one measurement is smaller than another."""
        if not isinstance(other, Measurement):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __add__(self, other: object) -> "Measurement":
        """Add two measurements and keep the unit of the left operand."""
        if not isinstance(other, Measurement):
            return NotImplemented
        converted_other = other.to_unit(self.unit)
        return Measurement(self.value + converted_other.value, self.unit)

    def __sub__(self, other: object) -> "Measurement":
        """Subtract one measurement from another
        
        Use the left operand's unit.
        """
        if not isinstance(other, Measurement):
            return NotImplemented
        converted_other = other.to_unit(self.unit)
        difference = self.value - converted_other.value
        if difference < 0:
            raise ValueError("Resulting measurement cannot be negative")
        return Measurement(difference, self.unit)
