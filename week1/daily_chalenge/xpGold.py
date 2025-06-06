#Exercise 1: What is the Season?
while True:
    month = int(input("Entrez un numéro de mois (1-12) : "))

    if month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Fall"
    elif month in [1, 2, 12]:
        season = "Winter"
    else:
        season = None

    if season:
        print(f"Le mois {month} correspond à la saison : {season}")
        break
    else:
        print("Numéro de mois invalide. Veuillez entrer un nombre entre 1 et 12.")


#Exercise 2: For Loop

for i in range(1, 21): print(i)
for i in range(1, 21, 2): print(i)

#Exercise 3: While Loop
name="Alex"
while True:
    nameInput = input("Donnez moi votre nom svp :) : ")
    if name == nameInput:
        print(f"Tu as exactement le même nom : {nameInput}")
        break
    else: print("Non")

#Exercise 4: Check the index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Entrez votre nom : ")

if user_name in names:
    index = names.index(user_name)
    print(f"La premiere occurence de '{user_name}' est à {index}.")
else:
    print(f"Désolé, '{user_name}' n'est pas dans la liste.")

#Exercise 5: Greatest Number

listNumber = []

for i in range(1, 4):
    listNumber.append(int(input(f"Mets le nombre {i} de la liste: ")))

print(f"Le nombre le plus grand est {max(listNumber)}")

#Exercise 6: Random number

import random

games_won = 0
games_lost = 0

while True:
    # Ask user for a number between 1 and 9
    guess = input("Choisi un chiffre entre 1 et 9 (ou marque quit pour arreter): ")

    if guess.lower() == 'quit':
        break

    if not guess.isdigit() or not (1 <= int(guess) <= 9):
        print("STP un chiffre entre 1 et 9")
        continue

    guess_num = int(guess)
    random_num = random.randint(1, 9)

    if guess_num == random_num:
        print("Bravo!")
        games_won += 1
    else:
        print(f"Raté le chiffre était {random_num}.")
        games_lost += 1

print("\nGame over!")
print(f"Victoire(s): {games_won}")
print(f"Défaite(s): {games_lost}")
