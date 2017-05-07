# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
#
#
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the inventory parameter
# is a dictionary representing the player’s inventory (like in the previous project) and the
# addedItems parameter is a list like dragonLoot.
# The addToInventory() function should return a dictionary that represents the updated inventory.

import fantasy_game_inventory

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory.get(item) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
fantasy_game_inventory.display_inventory(inv)
