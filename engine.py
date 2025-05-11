import random
import time
from utils import typewriter, safe_input, clear_screen,print_speaker,game_over, play_skill_gain_sound
from state import player, game_state
from combat.enemies import create_shouting_man, create_peter_practice1
from combat.battle_system import start_battle

# ───────────────────────────────────────────────
# ONE-TIME RANDOM EVENTS
# ───────────────────────────────────────────────

# Unarmored Event
def unarmored_event():
    """
    Triggered in Chapter 1 if the player does NOT equip the armor.
    40% chance of instant game over, 60% chance of +2 Strength.

    """
    typewriter("You begin to make your way to the village but feel an unnatural chill from the winds around you")
    time.sleep(0.3)
    typewriter("As you attempt to push through you hear voices whispering with in the winds")
    time.sleep(2)
    clear_screen()
    game_state["met_mysterious__wind_voice"] = True
    print_speaker("Voices of the Wind")
    typewriter("We shall not allow you past this point. The sword you carry is cursed and shall only bring suffering to these Isles.")
    time.sleep(1)
    typewriter("WE MUST ELIMINATE YOU")
    time.sleep(3)
    clear_screen()

    roll = random.randint(1, 100)

    if roll <= 40:
        typewriter("As the winds pick up you try your hardest to resist. The bitter cold feels like needles ripping into your skin.")
        time.sleep(0.5)
        typewriter("Though you tried your best to survive the cold has claimed you. Another soul has been lost.")
        time.sleep(0.5)
        print_speaker("Mysterious Voice")
        typewriter("Perhaps the next will be prove to worth my time.")
        time.sleep(0.5)
        game_over()
    else:
        typewriter("The storm rages on and you try your hardest to resist. The bitter cold feels like needles ripping into your skin but through some miracle you somehow survive")
        time.sleep(0.5)
        typewriter("The storm slowly subsides. You lean against a cliff not too far from the path you were walking to rest for a moment. The sword on your hip glows and the mysterious voice from before begin to speak")
        print_speaker("Mysterious Voice")
        typewriter("You were foolish to not wear what was given to you...")
        time.sleep(0.5)
        typewriter("But perhaps you're foolishness proves something.") 
        time.sleep(0.3)
        play_skill_gain_sound()
        typewriter("+2 Strength")
        player["stats"]["strength"] += 2
        time.sleep(0.5)
        typewriter("While there are others, you are important to this. I've imprinted the armor into your soul. Do not continue to treat your life so carelessly")
        player["armored"] = True
        player["inventory"].append("Eldrich Plate Armour")

# Drink at Bar Elena Event (Tavern option)
def bar_Scene_Tavern_Route():
    typewriter("")
    time.sleep(0.5)
    typewriter("")


  

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



# ───────────────────────────────────────────────
# Battle Functions
# - A place to create wrapper funtions for battles
#   - Mainly to be able to create save points
# ───────────────────────────────────────────────
def Peter_battle_tutorial():
    enemy = create_peter_practice1()
    start_battle(enemy, reward_gold=15, reward_item="Health Potion")