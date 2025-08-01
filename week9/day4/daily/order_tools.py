from collections.abc import Iterable
from random import randint
from typing import List
from langchain_core.tools import tool
from langchain_core.messages.tool import ToolMessage
from langgraph.graph import END

from core import OrderState


# 1. TOOLS: déclarés mais non exécutés ici
@tool
def add_to_order(drink: str, modifiers: Iterable[str]) -> str:
    """Adds the specified drink to the customer's order, including any modifiers."""


@tool
def confirm_order() -> str:
    """Asks the customer if the order is correct."""


@tool
def get_order() -> str:
    """Returns the users order so far. One item per line."""


@tool
def clear_order():
    """Removes all items from the user's order."""


@tool
def place_order() -> int:
    """Sends the order to the barista for fulfillment."""


# 2. NODE: traitement réel des outils
def order_node(state: OrderState) -> OrderState:
    msg = state["messages"][-1]
    tool_calls = msg.tool_calls
    order: List[str] = state.get("order", [])
    outbound_msgs = []
    order_placed = False

    for tool_call in tool_calls:
        name = tool_call["name"]
        args = tool_call["args"]
        response = None

        if name == "add_to_order":
            modifiers = args.get("modifiers", [])
            modifier_str = ", ".join(modifiers) if modifiers else "no modifiers"
            order.append(f'{args["drink"]} ({modifier_str})')
            response = "\n".join(order)

        elif name == "confirm_order":
            print("Your order:")
            if not order:
                print("  (no items)")
            for drink in order:
                print(f"  {drink}")
            response = input("Is this correct? ")

        elif name == "get_order":
            response = "\n".join(order) if order else "(no order)"

        elif name == "clear_order":
            order.clear()
            response = None

        elif name == "place_order":
            print("Sending order to kitchen!")
            print("\n".join(order))
            order_placed = True
            response = randint(1, 5)

        else:
            raise NotImplementedError(f"Unknown tool call: {name}")

        outbound_msgs.append(
            ToolMessage(
                content=response,
                name=name,
                tool_call_id=tool_call["id"],
            )
        )

    return {
        "messages": outbound_msgs,
        "order": order,
        "finished": order_placed,
    }


# 3. ROUTAGE conditionnel vers le bon nœud
def maybe_route_to_tools(state: OrderState, tool_node) -> str:
    msgs = state.get("messages", [])
    if not msgs:
        raise ValueError("No messages in state.")

    msg = msgs[-1]

    if state.get("finished", False):
        return END

    elif hasattr(msg, "tool_calls") and msg.tool_calls:
        if any(t["name"] in tool_node.tools_by_name for t in msg.tool_calls):
            return "tools"
        else:
            return "ordering"
    else:
        return "human"
