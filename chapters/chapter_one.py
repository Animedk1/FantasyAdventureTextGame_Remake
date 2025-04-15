import time
from state import player, game_state
from utils import typewriter, clear_screen, get_choice
from engine import unarmored_event
# ───────────────────────────────────────────────
# Choose (1) functions
# Notes:
#   - All three option lead you to talking with the sword
#   - Options that don't include equiping armor will lead you to a random death event
# ───────────────────────────────────────────────

def check_sword():
    typewriter("While reaching to grab the sword from the snow, you hear a voice calling to you.")
    game_state["met_mysterious_voice"] = True

def equip_armour():
    typewriter("You walk over and grab the armour from the snow.")
    typewriter("Upon closer inspection, you realize you've never seen armor made of this material.")
    typewriter("When placing the armour on your body, you're met with a feeling of dread—a burning sensation courses through you.")
    player["armored"] = True
    player["inventory"].append("Eldrich Plate Armour")

def check_fire():
    typewriter("You lean down and check the fire.")
    time.sleep(0.3)
    typewriter("It's too far gone. The embers are cold and dead.")
    time.sleep(1)
    player["stats"]["intelligence"] += 1
    clear_screen()
    typewriter("While looking at the fire, you hear a low ringing coming from behind you.")
    typewriter("Upon further inspection, you notice it's the sword.")
    check_sword()

def Chapter_one_start():
    player["checkpoint"] = "chapter_one"

    typewriter("Prologue: Awakening")
    time.sleep(2)
    typewriter("You wake up sitting in front of the ashes of a recently lit campfire.")
    time.sleep(0.3)
    typewriter("Your memory is hazy.")
    typewriter("Your back is pressed against a cold stone wall that once belonged to a small fortress within the land.")
    time.sleep(0.3)
    typewriter("Beside you lies your armour, in need of repair.\nBeside it is a sword with a faint red glow, buried in snow.")
    time.sleep(0.3)
    typewriter("You look toward the sky. A crimson moon sinks slowly behind the trees.\nDaylight is near, but the night is still bitter.")
    time.sleep(0.3)
    typewriter("You stand up and consider your next move...\n")

    print("a) Equip your armour")
    print("b) Inspect the small camp around you")
    print("c) Inspect the sword beneath the snow\n")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b", "c"])

    if choice == "a":
        equip_armour()
    elif choice == "b":
        check_fire()
    elif choice == "c":
        check_sword()

    if not player["armored"]:
        unarmored_event()
