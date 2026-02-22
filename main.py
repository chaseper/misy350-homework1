inventory = [
 {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
 {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
 {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
 {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
 {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
 {"order_id": "Order_101", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
 {"order_id": "Order_102", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75}
]


# MISY350 Homework 1 - Coffee Shop Kiosk


inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id": "Order_101", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
    {"order_id": "Order_102", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75},
]

def find_inventory_item_by_id(item_id):
    """Return the inventory item dictionary for a matching item_id, or None."""
    for inventory_item in inventory:
        if inventory_item["item_id"] == item_id:
            return inventory_item
    return None


def find_inventory_item_by_name(item_name):
    """Return the inventory item dictionary for a matching item name, or None."""
    for inventory_item in inventory:
        if inventory_item["name"].lower() == item_name.lower():
            return inventory_item
    return None


def find_order_by_id(order_id):
    """Return the order dictionary for a matching order_id, or None."""
    for customer_order in orders:
        if customer_order["order_id"] == order_id:
            return customer_order
    return None


def print_inventory():
    print("\nCurrent Inventory:")
    for inventory_item in inventory:
        print(
            f"ID: {inventory_item['item_id']} | "
            f"Name: {inventory_item['name']} | "
            f"Price: ${inventory_item['unit_price']:.2f} | "
            f"Stock: {inventory_item['stock']}"
        )


def print_orders():
    print("\nCurrent Orders:")
    for customer_order in orders:
        print(
            f"Order ID: {customer_order['order_id']} | "
            f"Item ID: {customer_order['item_id']} | "
            f"Qty: {customer_order['quantity']} | "
            f"Status: {customer_order['status']} | "
            f"Total: ${customer_order['total']:.2f}"
        )


# Query 1: Place a new order for an item and quantity.
# 1. Input:
print("\n--- CREATE | Query 1: Place a New Order ---")
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

# 2. Process: Validate and Create Order
selected_item = find_inventory_item_by_id(item_id)

if selected_item is None:
    # 3. Output:
    print("Error: Item ID not found.")
else:
    if quantity <= 0:
        print("Error: Quantity must be greater than 0.")
    elif selected_item["stock"] < quantity:
        print("Error: Not enough stock available.")
    else:
      
        selected_item["stock"] -= quantity

   
        order_total = quantity * selected_item["unit_price"]

    
        new_order_number = 101 + len(orders)
        new_order_id = f"Order_{new_order_number}"

        new_order = {
            "order_id": new_order_id,
            "item_id": item_id,
            "quantity": quantity,
            "status": "Placed",
            "total": order_total
        }
        orders.append(new_order)

        print(f"Success: Order placed -> {new_order_id}")
        print(f"{selected_item['name']} stock is now {selected_item['stock']}")



# Query 2: View all orders placed for a particular item (prompt for item name).
#1
print("\n--- READ | Query 2: View Orders by Item Name ---")
search_item_name = input("Enter the item name to search (e.g. 'Latte'): ")


matching_item = find_inventory_item_by_name(search_item_name)


if matching_item is None:
    print("Error: Item name not found in inventory.")
else:
    print(f"Orders for {matching_item['name']}:")
    found_orders = False

    for customer_order in orders:
        if customer_order["item_id"] == matching_item["item_id"]:
            print(
                f"- {customer_order['order_id']} | "
                f"Qty: {customer_order['quantity']} | "
                f"Status: {customer_order['status']} | "
                f"Total: ${customer_order['total']:.2f}"
            )
            found_orders = True

    if not found_orders:
        print("No orders found for this item.")


# Query 3: Calculate and print the total number of orders placed for "Cold Brew".
print("\n--- READ | Query 3: Count Orders for Cold Brew ---")
target_item_name = "Cold Brew"

cold_brew_item = find_inventory_item_by_name(target_item_name)
cold_brew_order_count = 0

if cold_brew_item is not None:
    for customer_order in orders:
        if customer_order["item_id"] == cold_brew_item["item_id"]:
            cold_brew_order_count += 1

print(f"Total number of orders placed for '{target_item_name}': {cold_brew_order_count}")


# Query 4: Update item stock quantity by item id.
print("\n--- UPDATE | Query 4: Update Stock ---")
update_item_id = int(input("Enter ID of item to update: "))
new_stock_quantity = int(input("Enter new stock quantity: "))

inventory_item_to_update = find_inventory_item_by_id(update_item_id)

if inventory_item_to_update is None:
    print("Error: Item ID not found.")
else:
    if new_stock_quantity < 0:
        print("Error: Stock cannot be negative.")
    else:
        inventory_item_to_update["stock"] = new_stock_quantity
        print(f"Success: {inventory_item_to_update['name']} stock updated to {new_stock_quantity}.")


# Query 5: Cancel an order and restore stock.
print("\n--- REMOVE / DELETE | Query 5: Cancel Order ---")
cancel_order_id = input("Enter Order ID to cancel: ")

order_to_cancel = find_order_by_id(cancel_order_id)


if order_to_cancel is None:
    print("Error: Order ID not found.")
else:
    if order_to_cancel["status"] == "Cancelled":
        print("This order is already cancelled.")
    else:

        order_to_cancel["status"] = "Cancelled"

        ordered_item_id = order_to_cancel["item_id"]
        ordered_quantity = order_to_cancel["quantity"]


        cancelled_item = find_inventory_item_by_id(ordered_item_id)
        if cancelled_item is not None:
            cancelled_item["stock"] += ordered_quantity
            print(f"Success: {cancel_order_id} cancelled.")
            print(f"{cancelled_item['name']} stock restored to {cancelled_item['stock']}.")
        else:
            print("Order cancelled, but matching inventory item was not found.")


print_inventory()
print_orders()