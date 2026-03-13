"""Measurement module for storing a value with a unit."""


class Measurement:
    """A class to represent a measurement with a numeric value and unit.

    Attributes:
        value: The numeric measurement value.
        unit: The unit of measurement (e.g. 'meters', 'centimeters').
    """

    VALID_UNITS: tuple[str, ...] = ("meters", "centimeters", "feet", "inches")

    def __init__(self, value: float, unit: str = "meters") -> None:
        """Initialize the measurement.

        Args:
            value: The numeric value of the measurement. Must be non-negative.
            unit: The unit of the measurement. Defaults to 'meters'.
                  Valid options: 'meters', 'centimeters', 'feet', 'inches'.

        Raises:
            ValueError: If value is negative or unit is not recognized.
        """
        if value < 0:
            raise ValueError(
                f"Measurement value must be non-negative, got {value}"
            )
        if unit not in self.VALID_UNITS:
            raise ValueError(
                f"Unit '{unit}' is not recognized. "
                f"Valid units are: {', '.join(self.VALID_UNITS)}"
            )
        self.value = value
        self.unit = unit

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"Measurement(value={self.value}, unit={self.unit!r})"

    def __str__(self) -> str:
        """Return a human-readable string of the measurement."""
        return f"{self.value} {self.unit}"
