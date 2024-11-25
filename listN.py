print("Eugene Hotel Menu")

restaurant_menu = [
    ["Appetizers", ["Garlic Bread","nuddles", "Onion Rings"]],
    ["Main Courses", ["Pizza", "Pasta", "Steak"]],
    ["Desserts", ["Ice Cream", "Cake", "Tiramisu"]]
]

for category, items in restaurant_menu:
    print(f"\n{category}:")
    for item in items:
        print(f"- {item}")