inventory = {}

def add_item(dictionary, name, item_quantity):
    if name in dictionary.keys():
        dictionary[name] += item_quantity
    else:
        dictionary.update({name:item_quantity})

add_item(inventory, "appel", 6)
add_item(inventory, "appel", 10)
add_item(inventory, "banana", 3)

print(inventory)