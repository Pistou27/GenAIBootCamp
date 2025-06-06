#1
print("Hello World\n" * 4)

#2
print((99**3)*8)

#3
def coolname():
    theName = "Alex"
    userName = input("C'est quoi ton prenom?")
    if theName.strip().lower() == userName.strip().lower():
        print("Oh mon dieu on a les mêmes prenoms, kyaaaaa <3")
    else:
        print(f"Comme c'est dommage, {theName} est plus beau de tout de façon")

coolname()

#4
def yourAreTall():
    height = int(input("Tu fais quelle taille (en cm)?"))
    if height >= 145:
        print("Bienvenu sur l'attraction le cassecou")
    else:
        print("Tu es trop petit le nabot")

yourAreTall()

#5
my_fav_numbers = {2, 4, 5, 32}
my_fav_numbers.add(64)
my_fav_numbers.add(128)
my_fav_numbers.remove(128)
friend_fav_numbers = {256, 512}
conc_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(conc_fav_numbers)

#6
tupleInt = (1,2,3,4)
#Immuable

#7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#8

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
sandwich_orders = [sandwitch for sandwitch in sandwich_orders if sandwitch != "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)

for preparation in finished_sandwiches:
    print(f"I made your {preparation}")
