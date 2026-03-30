"""
Module containing the Goal and Goals classes for tracking a person's 
goals.
"""

from __future__ import annotations


class Goal:
    """A class to represent an individual goal.

    Attributes:
        name: The name of the goal.
        description: A brief description of the goal.
        completed: Whether the goal has been completed.
    """

    def __init__(self, name: str, description: str = "") -> None:
        """Initialize the goal.

        Args:
            name: The name of the goal.
            description: A brief description of the goal. Defaults to "".

        Raises:
            TypeError: If name or description is not a string.
            ValueError: If name is empty.
        """
        if not isinstance(name, str):
            raise TypeError(
                f"Goal name must be a string, got {type(name).__name__}"
            )
        if not name.strip():
            raise ValueError("Goal name cannot be empty")
        if not isinstance(description, str):
            raise TypeError(
                f"Description must be a string, got "
                f"{type(description).__name__}"
            )

        self.name = name.strip()
        self.description = description.strip()
        self.completed = False

    def complete(self) -> None:
        """Mark the goal as completed."""
        self.completed = True

    def reset(self) -> None:
        """Reset the goal back to incomplete."""
        self.completed = False

    def __str__(self) -> str:
        """Return a string representation of the goal."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.name}"

    def __repr__(self) -> str:
        """Return a detailed representation of the goal."""
        return f"Goal(name={self.name!r}, completed={self.completed})"


class Goals:
    """A class to manage a collection of goals.

    Attributes:
        list: A list of Goal objects.
    """

    def __init__(self) -> None:
        """Initialize with an empty goals list."""
        self.list: list[Goal] = []

    def add_goal(self, name: str, description: str = "") -> Goal:
        """Add a new goal.

        Args:
            name: The name of the goal.
            description: A brief description. Defaults to "".

        Raises:
            ValueError: If a goal with the same name already exists.

        Returns:
            The newly created Goal.
        """
        if not isinstance(name, str):
            raise TypeError(
                f"Goal name must be a string, got {type(name).__name__}"
            )
        if any(g.name.lower() == name.strip().lower() for g in self.list):
            raise ValueError(
                f"Goal '{name}' already exists"
            )
        goal = Goal(name, description)
        self.list.append(goal)
        return goal

    def remove_goal(self, name: str) -> None:
        """Remove a goal by name.

        Args:
            name: The name of the goal to remove.

        Raises:
            ValueError: If no goal with that name exists.
        """
        goal = self._find_goal(name)
        self.list.remove(goal)

    def complete_goal(self, name: str) -> None:
        """Mark a goal as completed.

        Args:
            name: The name of the goal to complete.

        Raises:
            ValueError: If no goal with that name exists.
        """
        self._find_goal(name).complete()

    def pending_goals(self) -> list[Goal]:
        """Return a list of incomplete goals.

        Returns:
            List of Goal objects that are not yet completed.
        """
        return [g for g in self.list if not g.completed]

    def completed_goals(self) -> list[Goal]:
        """Return a list of completed goals.

        Returns:
            List of Goal objects that are completed.
        """
        return [g for g in self.list if g.completed]

    def is_goalless(self) -> bool:
        """Return True if there are no goals.

        Returns:
            True if the goals list is empty.
        """
        return len(self.list) == 0

    def summary(self) -> str:
        """Return a summary of all goals.

        Returns:
            A formatted string listing all goals and their status.
        """
        if self.is_goalless():
            return "No goals set."
        return "\n".join(str(g) for g in self.list)

    def _find_goal(self, name: str) -> Goal:
        """Find a goal by name.

        Args:
            name: The name of the goal to find.

        Raises:
            ValueError: If no goal with that name exists.

        Returns:
            The matching Goal object.
        """
        if not isinstance(name, str):
            raise TypeError(
                f"Goal name must be a string, got {type(name).__name__}"
            )
        for goal in self.list:
            if goal.name.lower() == name.strip().lower():
                return goal
        raise ValueError(f"Goal '{name}' not found.")

    def __str__(self) -> str:
        """Return a string representation of all goals."""
        return self.summary()

    def __repr__(self) -> str:
        """Return a detailed representation of the Goals collection."""
        return f"Goals(goals={self.list!r})"
