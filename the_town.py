"""Add yourself as a Person instance here!"""

from theperson.person import Person, Profile, Professional


if __name__ == "__main__":
    morpheus = Person(
        profile=Profile(name="Morpheus", gender="male"),
        professional=Professional(occupation="developer on GitHub"),
    )

    morpheus.introduce()

    syed = Person(
        profile=Profile(name="Syed Abdul Aman", gender="male"),
        professional=Professional(occupation="Generative AI Developer"),
    )

    syed.introduce()
    
    gloria = Person(
        profile=Profile(name="Gloria", gender="female"),
        professional=Professional(occupation="Data Scientist"),
    )       
    
    gloria.introduce()

    joe = Person(
        profile=Profile(
            name="Joe", 
            gender="male", 
            hobbies=["coding", "chess", "hiking"]
        ),
        professional=Professional(
            occupation="Product Owner", 
            skills=["product design", "prototyping"]
        )
    )

    joe.introduce()
    joe.mood.set_mood("calm", 0.9)
    joe.goals.add_goal("master git")
    joe.greet(morpheus)
