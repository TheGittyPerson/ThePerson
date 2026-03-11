from typing import TextIO


class Person:
    """A class to represent a person."""
    
    def __init__(self,
                 name: str | None = None,
                 age: int | None = None,
                 gender: str | None = None,
                 height: float | None = None,
                 nationality: str | None = None,
                 occupation: str | None = None) -> None:
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.nationality = nationality
        self.occupation = occupation
        self.calories = 2000
        self.fatigue = 100
        self.relations = {
            "Self" : self,
            "Friend" : [],
            "Mother" : [],
            "Father" : [],
            "Sister" : [],
            "Brother" : [],
            "Wife" : [],
            "Husband" : [],
            "Girlfriend" : [],
            "Boyfriend" : []
        }

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

        self.saturation -= 1

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

    def eat(self,calories) -> None:
        """ Increase the number of calories by eating food. """
        self.calories = min(self.calories+calories , 2000)

    def sleep(self) -> None:
        """ Resting gets rid of the fatigue. """
        self.fatigue = 100

    def add_relation(self, Person, Relation):
        """ Relationships between people. """
        if Relation in self.relations:
            self.relations[Relation].append(Person)
        else:
            self.relations[Relation] = [Person]

    