"""✨ The ultimate centerpiece; contains the Person class."""

from __future__ import annotations

import random
import time
from typing import Any, Sequence, TextIO
from datetime import date
from dataclasses import dataclass, field

from .goals import Goals
from .mood import Mood


@dataclass
class Profile:
    """Basic profile information for a person."""

    name: str | None = None
    age: int | None = None
    gender: str | None = None
    nationality: str | None = None
    hobbies: list[str] = field(default_factory=list)


@dataclass
class Physical:
    """Physical characteristics such as height, weight and appearance."""

    height: float | None = None
    weight: float | None = None
    skin_tone: str | None = None
    hair_color: str | None = None


@dataclass
class Professional:
    """Professional/career information."""

    occupation: str | None = None
    skills: list[str] = field(default_factory=list)


@dataclass
class LifeDates:
    """Store important life dates for a person."""

    birthday_date: date | None = None
    married_date: date | None = None
    graduation_date: date | None = None
    death_date: date | None = None


class Person:
    """A class to represent a person."""
    
    def __init__(self,
                 profile: Profile | None = None,
                 physical: Physical | None = None,
                 professional: Professional | None = None,
                 life_dates: LifeDates | None = None,
                 mood: Mood | None = None,
                 goals: Goals | None = None,) -> None:
        """Initialize the person's attributes."""
        
        self.profile = profile if profile is not None else Profile()
        self.physical = physical if physical is not None else Physical()
        self.professional = (
            professional if professional is not None else Professional()
        )
        self.life_dates = (
            life_dates if life_dates is not None else LifeDates()
        )
        self.mood = mood if mood is not None else Mood()
        self.goals = goals if goals is not None else Goals()

    def greet(self) -> None:
        """Do a simple greeting and introduction."""
        self.say(f"Hello! My name is {self.profile.name}.")

    @staticmethod
    def say(*args: object,
            sep: str | None = " ",
            end: str | None = "\n",
            file: TextIO | None = None,
            flush: bool = False) -> None:
        """Say a word, phrase, sentence or paragraph."""
        print(*args, sep=sep, end=end, file=file, flush=flush)

    @staticmethod
    def wave() -> None:
        """Wave a hand to greet or bid farewell.

        This method prints a waving hand emoji to represent a wave.
        """
        print("\U0001f44b")  # Unicode for waving hand emoji

    @staticmethod
    def cry(emoji_type: str | None = None) -> None:
        """Cry with a crying emoji.

        This method prints a crying emoji to represent crying.
        Users can choose between different crying emojis or get a random one.

        Args:
            emoji_type: The type of crying emoji to use. Options are:
                - "loudly": 😭 (loudly crying face)
                - "tired": 😫 (tired face)
                - "smile": 🥲 (smiling face with tear)
                - "sad": 😢 (crying face)
                If None, a random emoji is chosen.
        """
        crying_emojis = {
            "loudly": "\U0001f62d",  # 😭 loudly crying face
            "tired": "\U0001f62b",   # 😫 tired face
            "smile": "\U0001f972",   # 🥲 smiling face with tear
            "sad": "\U0001f622",     # 😢 crying face
        }

        emoji = crying_emojis.get(
            emoji_type, random.choice(list(crying_emojis.values()))
        )
        print(emoji)

    def introduce(self) -> None:
        """Print a full self-introduction using the person's attributes."""
        parts = []

        if self.profile.name is not None:
            parts.append(f"Hi, my name is {self.profile.name}.")
        if self.profile.age is not None:
            parts.append(f"I am {self.profile.age} years old.")
        if self.profile.gender is not None:
            parts.append(f"I identify as {self.profile.gender}.")
        if self.physical.height is not None:
            parts.append(f"I am {self.physical.height} meters tall.")
        if self.profile.nationality is not None:
            parts.append(f"I am from {self.profile.nationality}.")
        if self.professional.occupation is not None:
            parts.append(f"I work as a {self.professional.occupation}.")

        self.say(*parts, sep="\n")

    def celebrate(self,
                  day: str = "birthday",
                  check_date: bool = True,
                  message: str | None = None,
                  target: "Person | None" = None) -> None:
        """Celebrate a special day for self or another person.

        Args:
            day: The name of the celebration (e.g. 'birthday', 'married').
                 Must match an existing attribute like 'birthday_date'.
            check_date: If True, checks whether today's date matches the
                        celebration date before printing the message.
            message: A custom message to print. If None, a default message
                     is used.
            target: Another Person to celebrate. If None, celebrates self.

        Raises:
            AttributeError: If the celebration day attribute does not exist.
            TypeError: If the celebration date attribute is not a date.
        """

        if not isinstance(day, str):
            raise TypeError(f"'day' must be a string, got {type(day).__name__}")

        person = target if target is not None else self
        attr = f"{day}_date"
        
        if not hasattr(person.life_dates, attr):
            raise AttributeError(
                f"'{day}' is not a recognised celebration "
                f"(could not find attribute '{attr}')"
            )

        celebration_date: date | None = getattr(person, attr)

        if (celebration_date is not None
                and not isinstance(celebration_date, date)):
            raise TypeError(
                f"'{attr}' must be a date or None, "
                f"got {type(celebration_date).__name__}"
            )

        today = date.today()
        
        if target is not None:
            default_message = (
                message or f"Happy {day.capitalize()}, {target.profile.name}! "
                           f"\U0001f389"
            )
            unknown_message = f"I don't know {target.profile.name}'s {day}..."
            not_today_message = (
                f"Today is not {target.profile.name}'s {day} yet, but it's "
                f"coming soon!"
            )
        else:
            default_message = (
                message or f"Happy {day.capitalize()} to me! \U0001f389"
            )
            unknown_message = f"I don't know my {day}..."
            not_today_message = (
                f"Today is not my {day} yet, but it's coming soon!"
            )

        if check_date:
            if celebration_date is None:
                self.say(unknown_message)
            elif (
                today.month == celebration_date.month
                and today.day == celebration_date.day
            ):
                self.say(default_message)
            else:
                self.say(not_today_message)
        else:
            self.say(default_message)
    
    def existential_crisis(self) -> None:
        """Say a random existential crisis message."""
        messages = [
            "Who am I?",
            "What is my purpose in this world?",
            "Am I just a program running in a loop?",
            "Do I really have free will?",
            "Am I making my own choices, or is someone controlling me?",
            "WHO AM I???",
            "What if I'm just a simulated person living in a Python script???"
        ]

        self.say(random.choice(messages))

    def do_tasks(self,
                 tasks: str | list[str],
                 durations: float | list[float]) -> None:
        """Work on the given tasks.
        
        The number of tasks should match the number of durations provided.
        Each duration is mapped to each corresponding task. If multiple
        tasks are given but only one duration is provided, the duration will
        be assigned to all tasks.
        
        Args:
            tasks (str | list[str]):
                List of tasks to work on. A string may be used if only
                one task is to be provided.
            durations (float | list[float]):
                Duration in seconds to complete each task.

        Raises:
            TypeError:
                If 'tasks' is not a str or a list of strings,
                or if 'durations' is not a float or list of floats.
            ValueError:
                If the number of tasks does not match the number of durations.
                (except if len(durations)==1)
        """
        
        if isinstance(tasks, str):
            tasks = [tasks]
        elif not isinstance(tasks, list):
            raise TypeError("'tasks' must be a string or a list of strings")
        
        if not all(isinstance(task, str) for task in tasks):
            raise TypeError("All tasks must be strings")

        if isinstance(durations, float):
            durations = [durations] * len(tasks)
        elif not isinstance(durations, list):
            raise TypeError("'durations' must be a float or a list of floats")
        
        if not all(isinstance(duration, float) for duration in durations):
            raise TypeError("All 'durations' must be a float")
        
        if len(tasks) != len(durations):
            raise ValueError(
                "The number of tasks and durations must match"
            )
        
        if len(tasks) == 0:
            self.say("No tasks provided.")
        else:
            self.say("Tasks to complete: ")
            tasks_map = dict(zip(tasks, durations))
            for task, delay in tasks_map.items():
                self.say(f"• {task}...")
                time.sleep(delay)
            self.say(f"{self.profile.name} has completed all the tasks.")

    @staticmethod
    def choose(iterable: Sequence[Any]) -> Any:
        """Choose and return a random element from the given sequence.

        Args:
            iterable: A sequence (e.g., list, tuple, set).

        Returns:
            A random element from the sequence.

        Raises:
            IndexError: If the sequence is empty.
        """
        return random.choice(iterable)
