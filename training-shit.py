#!/usr/bin/env python3
"""
Simple single-file Pizza Ordering CLI.

Run:
    python pizza_order.py
"""
from dataclasses import dataclass, field
from typing import List
import sys

SIZE_MULTIPLIER = {"small": 1.0, "medium": 1.25, "large": 1.5}
EXTRA_TOPPING_COST = 0.5

MENU = [
    {"id": 1, "name": "Margherita", "base_price": 6.0, "default_toppings": ["tomato", "mozzarella", "basil"]},
    {"id": 2, "name": "Pepperoni",  "base_price": 7.5, "default_toppings": ["tomato", "mozzarella", "pepperoni"]},
    {"id": 3, "name": "Veggie",     "base_price": 7.0, "default_toppings": ["tomato", "mozzarella", "peppers", "onion"]},
    {"id": 4, "name": "Hawaiian",   "base_price": 8.0, "default_toppings": ["tomato", "mozzarella", "ham", "pineapple"]},
]

@dataclass
class Item:
    menu_item: dict
    size: str = "medium"
    extra_toppings: List[str] = field(default_factory=list)
    quantity: int = 1

    def price_per_pizza(self) -> float:
        base = self.menu_item["base_price"]
        mult = SIZE_MULTIPLIER.get(self.size, 1.0)
        extras = EXTRA_TOPPING_COST * len(self.extra_toppings)
        return round(base * mult + extras, 2)

    def subtotal(self) -> float:
        return round(self.price_per_pizza() * self.quantity, 2)


def prompt(prompt: str, default: str = "") -> str:
    res = input(f"{prompt} ").strip()
    if res == "" and default != "":
        return default
    return res

def prompt_int(prompt_text: str, default: int = None) -> int:
    while True:
        s = prompt(prompt_text, "" if default is None else str(default))
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")

def prompt_choice(prompt_text: str, choices: List[str], default: str = None) -> str:
    choices_str = "/".join(choices)
    while True:
        s = prompt(f"{prompt_text} ({choices_str})", default or "")
        s = s.lower()
        if s in choices:
            return s
        print("Invalid choice. Try again.")

def show_menu():
    print("\nMenu:")
    for m in MENU:
        dt = ", ".join(m["default_toppings"])
        print(f" {m['id']}. {m['name']} - ${m['base_price']:.2f} (default: {dt})")

def find_menu_item(item_id: int):
    for m in MENU:
        if m["id"] == item_id:
            return m
    return None

def choose_item() -> Item | None:
    show_menu()
    item_id = prompt_int("Enter pizza id to add to order (0 to cancel):", default=0)
    if item_id == 0:
        return None
    menu_item = find_menu_item(item_id)
    if not menu_item:
        print("Invalid id.")
        return None
    size = prompt_choice("Size", list(SIZE_MULTIPLIER.keys()), default="medium")
    extras = prompt("Extra toppings separated by comma (leave empty for none):", "")
    extra_list = [e.strip() for e in extras.split(",") if e.strip()]
    qty = prompt_int("Quantity:", default=1)
    return Item(menu_item=menu_item, size=size, extra_toppings=extra_list, quantity=qty)

def print_receipt(name: str, items: List[Item]):
    print("\n--- Receipt ---")
    print(f"Customer: {name}")
    total = 0.0
    for it in items:
        extras = ", ".join(it.extra_toppings) if it.extra_toppings else "none"
        ppp = it.price_per_pizza()
        sub = it.subtotal()
        print(f" - {it.quantity}x {it.menu_item['name']} ({it.size}), extras: {extras} -> ${sub:.2f}  (${ppp:.2f}/each)")
        total += sub
    print(f"Total: ${total:.2f}")
    print("---------------\n")

def main():
    print("Welcome to Simple Python Pizzeria (single-file)!")
    name = prompt("Customer name (leave empty for 'Anonymous'):", "Anonymous")
    order_items: List[Item] = []

    while True:
        print("\nOptions: [a]dd item  [v]iew receipt  [f]inish and exit  [q]uit without saving")
        cmd = prompt("Choose").lower()
        if cmd in ("q", "quit"):
            print("Goodbye.")
            sys.exit(0)
        if cmd in ("a", "add"):
            item = choose_item()
            if item:
                order_items.append(item)
                print(f"Added {item.quantity}x {item.menu_item['name']} ({item.size})")
            continue
        if cmd in ("v", "view"):
            if not order_items:
                print("No items yet.")
            else:
                print_receipt(name, order_items)
            continue
        if cmd in ("f", "finish"):
            if not order_items:
                print("No items added. Nothing to do. Goodbye.")
                sys.exit(0)
            print_receipt(name, order_items)
            print("Order complete. Thank you!")
            sys.exit(0)
        print("Unknown option. Try again.")

if __name__ == "__main__":
    main()