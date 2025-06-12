class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def __init__(self, name, age, eye_color="blue"):
        super().__init__(name, age)
        self.eye_color = eye_color

    def sing(self, sounds):
        return f'{sounds}'
    

bengal_obj = Bengal("Bounou", 3)
chartreux_obj = Chartreux("Loulou", 5)
siamese_obj = Siamese("Croucour", 9)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets=Pets(all_cats)

sara_pets.walk()

# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        first_dog_power_fight = self.weight * self.run_speed()
        other_dog_power_fight = other_dog.weight * other_dog.run_speed()

        if first_dog_power_fight > other_dog_power_fight:
            return f"{self.name} gagne contre {other_dog.name}"
        elif other_dog_power_fight > first_dog_power_fight:
            return f"{other_dog.name} gagne contre {self.name}"
        else:
            return "Egalité"


# Step 2: Create dog instances
dog1 = Dog("Rex", 5, 20)      
dog2 = Dog("Buddy", 3, 18)    
dog3 = Dog("Luna", 4, 22)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))
