from langgraph.graph import StateGraph, END
from langchain_core.messages.ai import AIMessage
from core import OrderState, BARISTABOT_SYSINT, llm, WELCOME_MSG
from tool import get_menu
from order_tools import (
    add_to_order,
    confirm_order,
    get_order,
    clear_order,
    place_order,
    order_node,
)
from langgraph.prebuilt import ToolNode

# --- Outils menu simples ---
simple_tools = [get_menu]
simple_tool_node = ToolNode(simple_tools)

# --- Outils commandes ---
order_tools = [
    add_to_order,
    confirm_order,
    get_order,
    clear_order,
    place_order,
]

# Wrapper pour utiliser order_node comme nœud du graphe
def order_node_wrapper(state: OrderState) -> OrderState:
    return order_node(state)

# LLM lié aux outils menu (optionnel)
llm_with_tools = llm.bind_tools(simple_tools)


def human_node(state: OrderState) -> OrderState:
    """Affiche le dernier message IA et lit la saisie utilisateur."""
    last_msg = state["messages"][-1]
    print("\n🤖 BaristaBot:", last_msg.content)

    user_input = input("👤 Vous : ")
    if user_input.strip().lower() in {"q", "quit", "exit", "goodbye"}:
        state["finished"] = True

    return state | {"messages": [("user", user_input)]}


def chatbot_with_welcome_msg(state: OrderState) -> OrderState:
    if state["messages"]:
        new_output = llm_with_tools.invoke([BARISTABOT_SYSINT] + state["messages"])
    else:
        new_output = AIMessage(content=WELCOME_MSG)

    return state | {"messages": [new_output]}


def routing_from_human(state: OrderState) -> str:
    if state.get("finished", False):
        return END

    last_msg = state["messages"][-1]

    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        # Si appel à un outil commande
        order_tool_names = {t.__name__ for t in order_tools}
        if any(tc["name"] in order_tool_names for tc in last_msg.tool_calls):
            return "ordering"
        # Sinon si appel à un outil simple menu
        elif any(tc["name"] == get_menu.name for tc in last_msg.tool_calls):
            return "tools"
        else:
            return "ordering"  # fallback
    return "chatbot"


# Construction du graphe
graph_builder = StateGraph(OrderState)

graph_builder.add_node("chatbot", chatbot_with_welcome_msg)
graph_builder.add_node("tools", simple_tool_node)
graph_builder.add_node("ordering", order_node_wrapper)
graph_builder.add_node("human", human_node)

graph_builder.set_entry_point("chatbot")
graph_builder.add_edge("chatbot", "tools")
graph_builder.add_edge("tools", "human")
graph_builder.add_edge("chatbot", "ordering")
graph_builder.add_edge("ordering", "human")
graph_builder.add_conditional_edges("human", routing_from_human)

chat_graph = graph_builder.compile()

with open("barista.png", "wb") as f:
    f.write(chat_graph.get_graph().draw_mermaid_png())
