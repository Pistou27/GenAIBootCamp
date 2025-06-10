import random
# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict_output = dict(zip(keys, values))
print(dict_output)

# Exercise 2: Cinemax #2

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8, 'babyMetal' : 2}
family = {}

while True:
    name = input("Entrer le nom de votre membre de famille (ou stop pour arrêter): ").strip()
    if name.lower() == "stop":
        break
    try:
        age = int(input(f"Entrez l'âge de {name}: ")) 
        family[name] = age
    except ValueError:
        print("Mettez un nombre ou un chiffre valide.")

total_cost = 0

for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{member.capitalize()}, {age} ans : ticket prix ${price}")
    total_cost += price
print(f"le prix total des tickets est de {total_cost}")

# Exercise 3: Zara
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
    }
}
brand['number_stores'] = 2
print(brand['type_of_clothes'])
brand['country_creation '] = 'Spain'
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
brand.pop("creation_date", None)
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

# Exercise 4 : Some Geography

def describe_city(city, country = "Unknown"):
 print(f"{city} is in {country}.")

describe_city("Paris", "France")
describe_city("Daggerfall")

# Exercise 5 : Random

def test_number(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else :
        print(f"Fail! Your number: {number}, Random number: {random_number}")

test_number(34)

# Exercise 6 : Let’s create some personalized shirts !

def make_shirt(size = "large", text= "I love Python"):
 print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Hello")

# Exercise 7 : Temperature Advice

def get_random_temp():
   return random.uniform(-10, 40)

def main():   
   random_temperature = get_random_temp()
   print(f"La température actuel est {random_temperature:.2f}°C.")
   if random_temperature < 0: print("Brrr, that’s freezing! Wear some extra layers today.")
   elif 0 <= random_temperature < 16: print("Quite chilly! Don’t forget your coat.")
   elif 16 <= random_temperature < 23: print("Nice weather.")
   elif 23 <= random_temperature < 32: print("A bit warm, stay hydrated.")
   else: print("It’s really hot! Stay cool.")

main()

# Exercise 8: Pizza Toppings
toppings = []
while True:
        topping = input("Entrez une garniture pour votre pizza (ou quit pour arrêter): ").strip()
        if topping.lower() == "quit":
            break
        if topping not in toppings:
            toppings.append(topping)
            print(f"Ajout {topping} sur votre pizza.")
        else : 
            print(f"{topping} est déjà présent")
print("Vous avez ajouter dans votre pizza : ")
for t in toppings:
    print(f"- {t}")     
print(f"Vous nous devez : {str(10 + 2.5*len(toppings))}$")

