from game import Game
def get_user_menu_choice():
    menu_options = {
        'g': 'Play a new game',
        's': 'Show scores',
        'x': 'Quit'
    }

    print("\nMenu:")
    for key, value in menu_options.items():
        print(f"({key}) {value}")

    choice = input("Votre choix: ").lower().strip()

    if choice in menu_options:
        return menu_options[choice]
    
    else:
        print("Choix Invalide.")
        return None
    
def print_results(results, end_game = False):
    print(f"""Résultats:
          
Victoire(s) {results.get("Victoire", 0)}
Défaite(s) {results.get("Défaite", 0)}
Egalité(s) {results.get("Egalité", 0)}""")
    if end_game:    
        print("\nMerci d'avoir joué (^o^)")
        print(r"""
   /////  
  | o o | 
 (|  ^  |)
  | [_] | 
   -----  
        """)
    
def main():
    results = {'Victoire': 0,
               'Défaite': 0,
               'Egalité': 0}

    while True:
        option_game = get_user_menu_choice()

        if option_game == "Quit":
            print_results(results, end_game=True)
            break

        elif option_game == "Show scores":
            print_results(results)
                
        elif option_game == "Play a new game":
            game = Game()        
            round = game.play()
            if round in results:
                results[round] += 1
            else:
                print(f"Résultat inconnu: {round}")
        
        else:
            print("Retour au menu")

main()
