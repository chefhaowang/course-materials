def sell_item(inventory, item_name, quantity):
    """
    Function to sell an item from the inventory.

    Args:
    inventory (dict): The store's inventory, where each key is an item name and 
                      each value is a dictionary containing the item's price, quantity, 
                      and restock threshold.
    item_name (str): The name of the item to sell.
    quantity (int): The quantity of the item to sell.

    Returns:
    float or str: The total price of the sale if successful, or a message if there is 
                  insufficient stock or if the item is not found.
    """
    if item_name in inventory:
        if inventory[item_name]["quantity"] >= quantity:
            total_price = inventory[item_name]["price"] * quantity

            inventory[item_name]["quantity"] -= quantity

            if inventory[item_name]["quantity"] < inventory[item_name]["restock_threshold"]:
                restock_item(inventory, item_name)

            return total_price
        else:
            return f"Insufficient stock for {item_name}. Only {inventory[item_name]['quantity']} left in stock."
    else:
        return f"Item {item_name} not found in inventory."


def restock_item(inventory, item_name):
    """
    Function to restock an item when its quantity falls below the threshold.

    Args:
    inventory (dict): The store's inventory, where each key is an item name and 
                      each value is a dictionary containing the item's price, quantity, 
                      and restock threshold.
    item_name (str): The name of the item to restock.

    This function increases the stock quantity of the item by a fixed amount (10 units).
    """
    print(f"Restocking {item_name}. Adding 10 more units.")

    inventory[item_name]["quantity"] += 10


def view_inventory(inventory):
    """
    Function to view the current state of the inventory.

    Args:
    inventory (dict): The store's inventory, where each key is an item name and 
                      each value is a dictionary containing the item's price, quantity, 
                      and restock threshold.

    This function prints each item’s name, price, current stock, and whether it needs to be restocked.
    """
    for item_name, details in inventory.items():
        restock_status = "Needs restocking" if details["quantity"] < details[
            "restock_threshold"] else "Stock is sufficient"

        print(f"{item_name}: Price: ${details['price']}, Quantity: {
              details['quantity']}, {restock_status}")


# Example usage:
# Initial inventory setup
inventory = {
    "Laptop": {"price": 1000, "quantity": 10, "restock_threshold": 5},
    "Phone": {"price": 800, "quantity": 15, "restock_threshold": 7},
    "Headphones": {"price": 150, "quantity": 25, "restock_threshold": 10},
    "Charger": {"price": 25, "quantity": 50, "restock_threshold": 20},
}

# Selling items from the inventory
print(f"Total sale price: ${sell_item(inventory, 'Laptop', 6):.2f} \n")

# View inventory after sale to see the updated quantities
view_inventory(inventory)

# Sell an item that triggers restocking
print(f"Total sale price: ${sell_item(inventory, 'Phone', 10):.2f} \n")

# View inventory again to see the restocked item
view_inventory(inventory)

