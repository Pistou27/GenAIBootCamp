import random

class Game:
    def get_user_item(self):
        items = {'p': 'pierre', 
                 'f': 'feuille', 
                 'c': 'ciseaux', 
                 'pierre': 'pierre', 
                 'feuille': 'feuille', 
                 'ciseaux': 'ciseaux'}
        user_item = None

        while user_item not in items:
            user_item = input("Selectionner (p)ierre, (f)euille, (c)isseaux: ").lower().strip()
            if user_item in items:
                return items[user_item]
            else:
                print("Choix invalide, Recommencez SVP (^o^)")

    def get_computer_item(self):
        return random.choice(['pierre', 'feuille', 'ciseaux'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "Egalité"
        elif (user_item == 'pierre' and computer_item == 'ciseaux') or \
             (user_item == 'feuille' and computer_item == 'pierre') or \
             (user_item == 'ciseaux' and computer_item == 'feuille'):
            return "Victoire"
        else :
            return "Défaite"        

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"""Vous avez sélectionnez : {user_item}. 
              L'ordinateur a selectionné : {computer_item}. 
              C'est une {result}!""")

        return result