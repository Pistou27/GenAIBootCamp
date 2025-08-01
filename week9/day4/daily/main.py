import os
from dotenv import load_dotenv
from core import OrderState
from chat_loop import chat_graph

def main():
    # Chargement des variables d'environnement depuis .env
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError("La variable GOOGLE_API_KEY est absente")

    # Fixe la variable d'environnement pour l'API Google (ou autre)
    os.environ["GOOGLE_API_KEY"] = api_key

    print("Bienvenue chez BaristaBot ☕. Tapez `q` pour quitter.")

    # État initial de la conversation
    initial_state: OrderState = {
        "messages": [],
        "order": [],
        "finished": False,
    }

    # Lance la boucle de dialogue avec l'état initial
    chat_graph.invoke(initial_state)


if __name__ == "__main__":
    main()
