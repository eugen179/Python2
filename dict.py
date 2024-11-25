inventory = {}

# Function to add a new product to the inventory
def add_product(name, price, quantity):
    inventory[name] = {'price': price, 'quantity': quantity}
    print(f"Product {name} added to inventory.")

# Function to update an existing product's information
def update_product(name, price=None, quantity=None):
    if name in inventory:
        if price is not None:
            inventory[name]['price'] = price
        if quantity is not None:
            inventory[name]['quantity'] = quantity
        print(f"Product {name} updated.")
    else:
        print(f"Product {name} not found in inventory.")

# Function to remove a product from the inventory
def remove_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product {name} removed from inventory.")
    else:
        print(f"Product {name} not found in inventory.")

# Function to display the current inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name, details in inventory.items():
            print(f"Name: {name}, Price: {details['price']}, Quantity: {details['quantity']}")

add_product('Apple', 1.5, 100)    
add_product('Banana', 0.8, 150)   
update_product('Apple', quantity=120)  
remove_product('Banana')         
display_inventory()            
