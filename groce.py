grocery_list = ["milk", "eggs", "bread", "apples"]

def display_list():
    print("Your grocery list:")
    for item in grocery_list:
        print(f"- {item}")

def add_item():
    item = input("Enter the item to add: ")
    grocery_list.append(item)
    print(f"{item} added to the list.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.") 
def modify_item():
    old_item = input("Enter the item to modify: ")
    new_item = input("Enter the new item: ")
    if old_item in grocery_list:
        index = grocery_list.index(old_item)
        grocery_list[index] = new_item
        print(f"{old_item} replaced with {new_item}.")
    else:
        print(f"{old_item} not found in the list.")

while True:
    print("\nOptions:")
    print("1. Display list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Modify item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        modify_item()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")