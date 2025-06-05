import random
## Number Guessing Game Project

def checkNumber():
    while True:
        try:
            number = int(input("Un nombre ENTRE 1 et 100 ----> "))
            break
        except ValueError:
            print("C'est pas un nombre!")
    return number

def number_guessing_game():
    #Declaration des informations
    random_number = random.randint(1, 100)
    max_attempts = 7

    for essay in range(max_attempts):

        number = checkNumber()

        if number == random_number:
            print (f"Tu es trop fort tu as trouver le bon nombre qui était {number}")
            break

        elif number < random_number: 
            print ("trop bas!")

        else: 
            print ("trop haut!")

        if essay != (max_attempts-1):
            print(f"Il te reste {max_attempts - (essay+1)} essais \(°_°)/ !")
        else :
            print(f"Tu as perdu la réponse était {random_number}")

number_guessing_game()

