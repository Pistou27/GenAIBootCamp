class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animals(self, animal_type, count = 1):
        if animal_type not in self.animals:
            self.animals[animal_type] = count
        else:
            self.animals[animal_type] += count
    
    def get_info(self):
        info = f"La ferme {self.name}\n\n"
        
        for animal, count in self.animals.items():
          info += f"{animal}: {count}\n"
        info += "\nE-I-E-I-0!"
        return info
    
    def get_animal_types(self):        
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        list_animal = self.get_animal_types()
        info = f"La ferme {self.name} a "

        for i, animal in enumerate(list_animal):
            count = self.animals[animal]
            info += f"{animal}s" if count > 1 else f"{animal}"
            if i == len(list_animal)-2: 
                info += " et "
            elif i == len(list_animal)-1:
                info += "."
            else: 
                info += ", "
        return info
            
        

farm = Farm("toto")

farm.add_animals("cochon", 23)
farm.add_animals("vache", 19)
farm.add_animals("cochon", 82)
farm.add_animals("poulet", 143)
farm.add_animals("mouton", 12)
farm.add_animals("chien", 1)

print(farm.get_info())

print(farm.get_animal_types())

print(farm.get_short_info())