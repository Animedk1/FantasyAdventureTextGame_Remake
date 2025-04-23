import time
from state import player, game_state
from utils import typewriter, clear_screen, get_choice
from engine import unarmored_event
from utils import play_skill_gain_sound, print_speaker
# ───────────────────────────────────────────────
# Choice (1) functions
# Notes:
#   - All three option lead you to talking with the sword
# ───────────────────────────────────────────────

def check_sword():
    clear_screen()
    typewriter("As you reach out to grab the sword from the snow, you feel a sharp pain in your chest")
    time.sleep(0.3)
    typewriter("The sensation is so strong it brings you to your knees")
    time.sleep(0.3)
    typewriter("As you look up from staring down at the ground you realize the feeling of the bitter cold has dissipated... ")
    time.sleep(0.3)
    typewriter("The world in front of you has changed.")
    time.sleep(0.3)
    typewriter("A blood red hue covers the sky and you find yourself standing atop a tower built of the a dark unknown material. ")
    time.sleep(0.3)
    typewriter("Behind you is a sealed door.")
    time.sleep(0.3)
    typewriter("Before you can bring yourself to investigate you hear a powerful forboding voice coming from the sky.")
    time.sleep(2)
    typewriter("You try to collect yourself, but find that you are unable to move")
    time.sleep(1)
    clear_screen()
    game_state["met_mysterious_voice"] = True
    print_speaker("Mysterious Voice")
    time.sleep(1)
    typewriter("Your time is short here so listen.")
    time.sleep(0.5)
    typewriter("You will understand with time but you are not the first to have been gifted with my power.")
    time.sleep(0.5)
    typewriter("We shall hope you will be the last")
    time.sleep(0.5)
    typewriter("A plague has spread throughout the isles from which you hail. So far as to reach within my domain")
    time.sleep(0.5)
    typewriter("The isles must burn and you need to be the one to ignite the flame")
    time.sleep(0.5)
    typewriter("Take the sword I've given you to the capital city of Aedros")
    time.sleep(0.5)
    typewriter("You are not my only chosen, but you are important. If you value your life and the lives of those you will soon meet, I caution you to take this task seriously ")
    time.sleep(2)
    clear_screen()
    print_speaker("Mysterious Voice")
    typewriter("Do not disappointment by being as disposable as the rest")
    time.sleep(4)
    clear_screen()
    typewriter("The world around you fades and you find yourself back in the snowy environment you were in before")
    time.sleep(0.5)


def equip_armour():
    clear_screen()
    typewriter("You grab the armour from the snow.")
    time.sleep(0.3)
    typewriter("Upon closer inspection, you realize you've never seen armor made of this material.")
    time.sleep(0.3)
    typewriter("When placing the armour on your body, you're met with a feeling of dread—a burning sensation courses through you.")
    time.sleep(0.3)
    typewriter("The armor begins to dissipates within your skin and a red symbol is burned into the palm of your hand")
    time.sleep(0.3)
    typewriter("Although the armor isn't visible you can still feel it's protection")
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
    typewriter("Upon further inspection you can tell this place was abandoned some time ago...though exactly how long, you can't quite tell")
    time.sleep(0.3)
    #Notification Sound
    play_skill_gain_sound()
    typewriter("(+1 intelligence)")
    player["stats"]["intelligence"] += 1
    typewriter("While taking in the environment around you, you hear a feint noise that echoes that of a whisper.")
    time.sleep(0.3)
    typewriter("Upon further inspection, you notice it's the sword.")
    time.sleep(1)
    check_sword()

def equip_armor_scene_1():
    typewriter("You look down at the armor laying in the snow and winder your next move...")
    print("a) Equip the armour")
    print("b) Continue without it")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b"])

    if choice =="a":
        equip_armour()
        player["armored"] = True
        player["inventory"].append("Eldrich Plate Armour")
    elif choice == "b":
        typewriter("You've chosen to leave the armor behind")

# ───────────────────────────────────────────────
# Choice (2) functions
# ───────────────────────────────────────────────
def travel_to_inn():
    typewriter("")


def travel_to_tavern():
    typewriter("")







# Game Narrative Start
# ───────────
# ───────────────────────────────────────────────
# Scene 1: 
# - 
# - Potential Skill Gains
#   - +1 INT
#   - +2 STR
# ───────────────────────────────────────────────    
def Chapter_one_start():
    player["checkpoint"] = "chapter_one"

    typewriter("Prologue: Awakening")
    time.sleep(2)
    typewriter("You wake up sitting in front of the ashes of a recently lit campfire.")
    time.sleep(0.3)
    typewriter("Your memory is hazy.")
    time.sleep(0.3)
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
# ───────────────────────────────────────────────
# Last Chance to equip armor
# ───────────────────────────────────────────────
    if not player["armored"]:
        equip_armor_scene_1()

# ───────────────────────────────────────────────
# Bonus Encounter if not armored
# ───────────────────────────────────────────────
    if not player["armored"]:
        unarmored_event()
#Start of Scene 2
    chapter_one_scene2()


def chapter_one_scene2():
    typewriter("As you approach the village, ")

# ───────────────────────────────────────────────
# Scene 2: Story Branch - Bath house
# - Major Event: Meet Markus
# - Major SKill Checks: STR.
# - Potential Skill Gains
#   - 
# ───────────────────────────────────────────────    




# ───────────────────────────────────────────────
# Sceene 2: Story Branch - Tavern
# - Major Events: Questioned by Armor, Meet Erena, 
# - Major Skill Checks: INT. 
# - Potential Skill Gains
#   - 
# ───────────────────────────────────────────────