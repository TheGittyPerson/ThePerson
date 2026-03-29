"""
Module containing the Mood class for tracking a person's emotional 
state.
"""

from __future__ import annotations


VALID_MOODS = {
    "neutral",
    "happy",
    "sad",
    "angry",
    "anxious",
    "excited",
    "tired",
    "surprised",
    "disgusted",
    "fearful",
    "calm",
    "confused",
}


class Mood:
    """A class to represent and manage a person's mood.

    Attributes:
        name: The name of the current mood (e.g. 'happy', 'sad').
        intensity: A decimal from 0 to 1 representing mood intensity.
                   'neutral' always has an intensity of 0.
    """

    def __init__(self,
                 name: str = "neutral",
                 intensity: float = 0.0) -> None:
        """Initialize the mood.

        Args:
            name: The name of the mood. Defaults to 'neutral'.
            intensity: The intensity of the mood, between 0 and 1.
                       Defaults to 0.0.

        Raises:
            ValueError: If the mood name is not recognised or intensity
                        is out of range.
        """
        self.name = Mood._validate_name(name)
        self.intensity = self._validate_intensity(intensity)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_name(name: str) -> str:
        """Validate and return the mood name.

        Args:
            name: The mood name to validate.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is not a recognised mood.

        Returns:
            The validated mood name.
        """
        if not isinstance(name, str):
            raise TypeError(
                f"Mood name must be a string, got {type(name).__name__}."
            )
        name = name.lower().strip()
        if name not in VALID_MOODS:
            raise ValueError(
                f"'{name}' is not a recognised mood. "
                f"Valid moods are: {', '.join(sorted(VALID_MOODS))}."
            )
        return name

    def _validate_intensity(self, intensity: float) -> float:
        """Validate and return the mood intensity.

        Args:
            intensity: The intensity value to validate.

        Raises:
            TypeError: If intensity is not a float or int.
            ValueError: If intensity is outside [0, 1].

        Returns:
            The validated intensity as a float.
        """
        if not isinstance(intensity, (int, float)):
            raise TypeError(
                f"Intensity must be a number, got {type(intensity).__name__}."
            )
        intensity = float(intensity)
        if not 0.0 <= intensity <= 1.0:
            raise ValueError(
                f"Intensity must be between 0 and 1, got {intensity}."
            )
        if self.name == "neutral":
            return 0.0
        return intensity

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def set_mood(self, name: str, intensity: float = 0.5) -> None:
        """Change the current mood.

        Args:
            name: The new mood name.
            intensity: The intensity of the new mood. Defaults to 0.5.
        """
        self.name = Mood._validate_name(name)
        self.intensity = self._validate_intensity(intensity)

    def intensify(self, amount: float = 0.1) -> None:
        """Increase the mood intensity by a given amount.

        Args:
            amount: How much to increase intensity by. Defaults to 0.1.

        Raises:
            ValueError: If amount is negative or mood is neutral.
        """
        if amount < 0:
            raise ValueError(
                "Amount must be non-negative. Use calm_down() to decrease "
                "intensity."
            )
        if self.name == "neutral":
            raise ValueError(
                "Cannot intensify a neutral mood. Use set_mood() first."
            )
        self.intensity = min(1.0, self.intensity + amount)

    def calm_down(self, amount: float = 0.1) -> None:
        """Decrease the mood intensity by a given amount.

        If intensity reaches 0, the mood resets to 'neutral'.

        Args:
            amount: How much to decrease intensity by. Defaults to 0.1.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.intensity = max(0.0, self.intensity - amount)
        if self.intensity == 0.0:
            self.name = "neutral"

    def reset(self) -> None:
        """Reset the mood back to neutral with zero intensity."""
        self.name = "neutral"
        self.intensity = 0.0

    def is_positive(self) -> bool:
        """Return True if the mood is generally positive.

        Returns:
            True if the mood is happy, excited, calm, or surprised.
        """
        return self.name in {"happy", "excited", "calm", "surprised"}

    def is_negative(self) -> bool:
        """Return True if the mood is generally negative.

        Returns:
            True if the mood is sad, angry, anxious, tired, disgusted,
            fearful, or confused.
        """
        return self.name in {"sad", "angry", "anxious", "tired",
                             "disgusted", "fearful", "confused"}

    def describe(self) -> str:
        """Return a human-readable description of the current mood.

        Returns:
            A string describing the mood and its intensity.
        """
        if self.name == "neutral":
            return "feeling neutral."
        intensity_label = (
            "slightly" if self.intensity < 0.4
            else "moderately" if self.intensity < 0.7
            else "very"
        )
        return (f"feeling {intensity_label} {self.name} "
                f"(intensity: {self.intensity:.2f}).")

    def __str__(self) -> str:
        """Return a string representation of the mood."""
        return self.describe()

    def __repr__(self) -> str:
        """Return a detailed representation of the mood."""
        return f"Mood(name={self.name!r}, intensity={self.intensity})"
