from typing import TextIO
from datetime import datetime, date


class Person:
    """A class to represent a person."""
    
    def __init__(self,
                 name: str | None = None,
                 age: int | None = None,
                 gender: str | None = None,
                 height: float | None = None,
                 nationality: str | None = None,
                 occupation: str | None = None,
                 birthday_date: date | None = None,
                 married_date: date | None = None,
                 graduation_date: date | None = None,
                 death_date: date | None = None, ) -> None:
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.nationality = nationality
        self.occupation = occupation
        self.birthday_date = birthday_date
        self.married_date = married_date
        self.graduation_date = graduation_date
        self.death_date = death_date

    def greet(self) -> None:
        """Do a simple greeting and introduction."""
        self.say(f"Hello! My name is {self.name}.")

    @staticmethod
    def say(*args: object,
            sep: str | None = " ",
            end: str | None = "\n",
            file: TextIO | None = None,
            flush: bool = False) -> None:
        """Say a word, phrase, sentence or paragraph."""
        print(*args, sep=sep, end=end, file=file, flush=flush)

    def introduce(self) -> None:
        """Print a full self-introduction using the person's attributes."""
        intro = f"Hi, my name is {self.name}."
        if self.age is not None:
            intro += f" I am {self.age} years old."
        if self.gender is not None:
            intro += f" I identify as {self.gender}."
        if self.height is not None:
            intro += f" I am {self.height} meters tall."
        if self.nationality is not None:
            intro += f" I am from {self.nationality}."
        if self.occupation is not None:
            intro += f" I work as a {self.occupation}."
        self.say(intro)

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
            TypeError: If the celebration date attribute is not a datetime or
                       is None.
        """
        if not isinstance(day, str):
            raise TypeError(f"'day' must be a string, got {type(day).__name__}")

        person = target if target is not None else self
        attr = f"{day}_date"
        if not hasattr(person, attr):
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

        today = datetime.today()
        if target is not None:
            default_message = (
                message or f"Happy {day.capitalize()}, {target.name}! "
                           f"\U0001f389"
            )
            unknown_message = f"I don't know {target.name}'s {day}..."
            not_today_message = (
                f"Today is not {target.name}'s {day} yet, but it's coming "
                f"soon!"
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
    