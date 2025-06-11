# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age



little_cat = Cat("Tom", 3)
middle_cat = Cat("Jerry", 10)
older_cat = Cat("Loulou", 14)

def find_oldest_cat(cat_1, cat_2, cat_3):
    oldest = max([cat_1, cat_2, cat_3], key=lambda cat: cat.age)
    return oldest

oldest_cat = find_oldest_cat(little_cat, middle_cat, older_cat)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#  Exercise 2 : Dogs
class Dog:
    def __init__(self, dog_name, height):
        self.name = dog_name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.height * 2} jumps cm high!")

davids_dog = Dog("David", 34)
sarahs_dog = Dog("Sarah", 45)

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

def compare_height(dog1, dog2):
    return max([dog1, dog2], key=lambda dog: dog.height)

dog_heighter = compare_height(davids_dog, sarahs_dog)

print(f"The heighter dog is {dog_heighter.name}")

# Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics_song):
        self.lyrics = lyrics_song
    
    def sing_me_a_song(self):
        for ligne in self.lyrics : 
            print(ligne)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name, animal_list):
        self.name = zoo_name
        self.animals = animal_list
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"Ajout de {new_animal} dans le zoo")
        else:
            print(f"{new_animal} est déjà présent dans le zoo: {self.name}")

    def get_animals(self):
        if not self.animals:
            print("Pas d'animaux à {self.name}")
        else:            
            for animal in self.animals:
                print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold not in self.animals:
            print("Pas de {animal_sold} dans le zoo")
        else:
            self.animals.remove(animal_sold)
            print(f"Extradition de {animal_sold} du zoo")

    def sort_animals(self):
        sorted_dict_animals = {}
        if not self.animals:
            print("Pas d'aimaux dans le zoo")
            return sorted_dict_animals
        else:
            for animal in sorted(self.animals):
                first_letter = animal[0].upper()
                if first_letter not in sorted_dict_animals:
                    sorted_dict_animals[first_letter] = []
                sorted_dict_animals[first_letter].append(animal)
        return sorted_dict_animals     

    def get_groups(self):
        dict_animals = self.sort_animals()
        for letter in dict_animals:
            print(f"{letter}: {dict_animals[letter]}")

# zoo = Zoo("Totoro", [])

# zoo.add_animal("Gorille")
# zoo.add_animal("Lion")

# zoo.get_animals()

# zoo.sell_animal('Lion')

# zoo.get_animals()

# zoo.add_animal("Lion")
# zoo.add_animal("Vache")
# zoo.add_animal("Lamentin")
# zoo.add_animal("Kakatoes")

# zoo.get_groups()