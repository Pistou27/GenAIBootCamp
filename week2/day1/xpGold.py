# Exercise 1: Birthday Look-up / Exercise 2: Birthdays Advanced

birthdays = {
    "Alice": "1990/05/23",
    "Bob": "1985/11/12",
    "Charlie": "1992/07/08",
    "Diana": "2000/03/17",
    "Ethan": "1998/09/30"
}
print("Bonjour vous pouvez consulter les dates d'anniversaire des personnes de la liste ci-dessous :")
for k in birthdays.keys() : print(f"- {k}")
name_find = input("Donnez moi un nom de personne : ").strip()
if name_find.capitalize() not in birthdays:
    print(f"Pas dans la liste pour {name_find}!")
else:
    print(f"La date d'anniversaire de {name_find.capitalize()} est {birthdays[name_find.capitalize()]}")

# Exercise 3: Check the index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

def test_name_and_index(name):
    if name in names:
        print(f"La première occurence de {name} est à l'index {names.index(name)}")
    else:
        print(f"Désolé {name} n'est pas présent dans la liste")

user_name= input(f"Entrez votre nom : ")
test_name_and_index(user_name)