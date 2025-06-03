while True:
    try:
        human_year = int(input("Mettez un âge d'humain "))
        if human_year < 1:
            print(f"l'âge de l'humain: {human_year} doit être supérieur ou égal à 1")
            continue
        break
    except ValueError:
        print("Valeur incompatible, votre valeur n'est pas un nombre ")


if human_year > 1:
    print(f"Les différents âges (/ans) des humains : {human_year}, chats : " + str(24 + 4*(human_year - 2)) + ", chiens : " + str(24 + 5*(human_year - 2)))
else:
    print(f"Les différents âges (/ans) des humains : {human_year}, chats : 15, chiens : 15")