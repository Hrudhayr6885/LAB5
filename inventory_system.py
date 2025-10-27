"""
inventory_system.py

A simple inventory management system that allows adding, removing,
loading, saving, and checking item quantities from a JSON file.
"""

import json
from datetime import datetime

# Global variable to store inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add a given quantity of an item to the stock.

    Args:
        item (str): Name of the item.
        qty (int): Quantity to add.
        logs (list): Optional list to record operation logs.
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a given quantity of an item from the stock.

    Args:
        item (str): Name of the item.
        qty (int): Quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """
    Get the quantity available for a specific item.

    Args:
        item (str): Name of the item.

    Returns:
        int: Quantity of the item.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): File path to load data from.
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """
    Save the current inventory data to a JSON file.

    Args:
        file (str): File path to save data into.
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """
    Print all items and their quantities.
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Check for items that have stock below a certain threshold.

    Args:
        threshold (int): Minimum quantity threshold.

    Returns:
        list: Items with quantity below the threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstrate basic inventory operations."""
    add_item("apple", 10)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
