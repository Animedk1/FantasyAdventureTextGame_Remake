import time
from state import player, game_state
from utils import typewriter, clear_screen, get_choice
from engine import unarmored_event
# ───────────────────────────────────────────────
# Choice (1) functions
# Notes:
#   - All three option lead you to talking with the sword
#   - Options that don't include equiping armor will lead you to a random death event
# ───────────────────────────────────────────────

def check_sword():
    clear_screen()
    typewriter("You readh out to grab the sword but before you do")
    game_state["met_mysterious_voice"] = True

def equip_armour():
    clear_screen()
    typewriter("You walk over and grab the armour from the snow.")
    time.sleep(0.3)
    typewriter("Upon closer inspection, you realize you've never seen armor made of this material.")
    time.sleep(0.3)
    typewriter("When placing the armour on your body, you're met with a feeling of dread—a burning sensation courses through you.")
    time.sleep(0.3)
    player["armored"] = True
    player["inventory"].append("Eldrich Plate Armour")
    check_sword()

def check_fire():
    clear_screen()
    typewriter("You lean down and check the fire.")
    time.sleep(0.3)
    typewriter("It's too far gone. The embers are cold and dead.")
    time.sleep(0.3)
    typewriter("After inspecting the fire you see the snow is covering the remains of what looks like was once a campsite")
    time.sleep(0.3)
    typewriter("Upon further inspection you can tell this place was abandonded some time ag...though exactly how long, you can't quite tell (+1 intelligence)")
    player["stats"]["intelligence"] += 1
    typewriter("While taking in the environemt around you, you hear a fient noise that echoes that of a whisper.")
    time.sleep(0.3)
    typewriter("Upon further inspection, you notice it's the sword.")
    check_sword()

    # ───────────────────────────────────────────────
# Choice (2) functions
# Notes:
#   - All three option lead you to talking with the sword
#   - Options that don't include equiping armor will lead you to a random death event
# ───────────────────────────────────────────────

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
