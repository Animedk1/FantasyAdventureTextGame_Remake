import random
from utils import typewriter, safe_input, clear_screen
from state import player, game_state

# ───────────────────────────────────────────────
# ONE-TIME RANDOM EVENTS
# ───────────────────────────────────────────────

def unarmored_event():
    """
    Triggered in Chapter 1 if the player does NOT equip the armor.
    40% chance of instant game over, 60% chance of +2 Strength.
    """
    typewriter("Without your armor, the icy wind cuts deeper than expected...")
    typewriter("You collapse briefly from the cold...")
    roll = random.randint(1, 100)

    if roll <= 40:
        typewriter("Your vision fades. The cold has claimed you.")
        typewriter("GAME OVER")
        exit()
    else:
        typewriter("But your will hardens through the suffering...")
        typewriter("You stand taller, stronger. (+2 Strength)")
        player["stats"]["strength"] += 2


# ───────────────────────────────────────────────
# SHOP SYSTEM
# ───────────────────────────────────────────────

shop_inventory = {
    "Health Potion": 15,
    "Torch": 10,
    "Rusty Dagger": 25,
    "Mana Flask": 20
}

def open_shop():
    """
    Opens the shop if it has been unlocked via story.
    """
    if not game_state.get("shop_unlocked", False):
        typewriter("You don't know where any shops are yet.")
        return

    while True:
        clear_screen()
        typewriter("Welcome to the Marketplace")
        typewriter("You currently have {} gold.".format(player["gold"]))
        typewriter("Items for sale:\n")

        for idx, (item, price) in enumerate(shop_inventory.items(), start=1):
            print(f"{idx}) {item} - {price} gold")

        print("\nType the item number to purchase or type 'exit' to leave the shop.")

        choice = safe_input("→ ").lower()

        if choice == "exit":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(shop_inventory):
            item = list(shop_inventory.keys())[int(choice) - 1]
            price = shop_inventory[item]

            if player["gold"] >= price:
                player["gold"] -= price
                player["inventory"].append(item)
                typewriter(f"You purchased a {item}.")
            else:
                typewriter("You don't have enough gold.")
        else:
            typewriter("Invalid selection. Please try again.")


# ───────────────────────────────────────────────
# RELATIONSHIP TRACKING
# ───────────────────────────────────────────────

def modify_relationship(name: str, value: int):
    """
    Adds or subtracts relationship points with a character.
    """
    if name in player["relationships"]:
        player["relationships"][name] += value
        player["relationships"][name] = max(0, min(100, player["relationships"][name]))  # clamp between 0-100
        typewriter(f"{name}'s bond is now {player['relationships'][name]}/100.")
    else:
        typewriter(f"Relationship with {name} does not exist.")
