from xp import Dog
import random
# Exercise 3: Dogs Domesticated

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs_name = list(args)
        print(f"{', '.join(dogs_name)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
    
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.last_name = ""
        self.age = age

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):        
        print(f"Family: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name}, {person.age} years old")

johnson_family = Family("Johnson")

johnson_family.born("Emily", 22)
johnson_family.born("Jake", 16)
johnson_family.born("Liam", 18)

johnson_family.check_majority("Emily")
johnson_family.check_majority("Jake")
johnson_family.check_majority("Liam")

johnson_family.family_presentation()


        

