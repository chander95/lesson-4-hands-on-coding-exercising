#Use while loops, lists, and if statements in python to simulate a coffee machine that offers different coffee types until the reservoir is empty

menu_items = ["Espresso shot", "Americano", "Frappe", "Hot Tea", "Iced Tea", "Cuppaccino", "Flat White", "Latte"]

for item in menu_items:
    while menu_items.index(item) < len(menu_items):
        print("I recommend a " + item)
        break





