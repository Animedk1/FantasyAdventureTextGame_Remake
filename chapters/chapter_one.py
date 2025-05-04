import time
from state import player, game_state
from utils import typewriter, clear_screen, get_choice
from engine import unarmored_event
from utils import play_skill_gain_sound, print_speaker, perform_save,switch_music

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
    typewriter("The pain you previous felt has subsided and you now have full control of your body")
    time.sleep(0.5)
    typewriter("-- something shows you the way to the village")
    time.sleep(0.5)
    typewriter("You prepare to set off on the path to the village that was shown to you")

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

def equip_armour_after_Sword():
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
    typewriter("You look down at the armor laying in the snow and think about your next move...")
    print("a) Equip the armour")
    print("b) Continue without it")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b"])

    if choice =="a":
        equip_armour_after_Sword()
        player["armored"] = True
        player["inventory"].append("Eldrich Plate Armour")
    elif choice == "b":
        typewriter("You've chosen to leave the armor behind")

# ───────────────────────────────────────────────
# Choice (2) functions
# ───────────────────────────────────────────────
def travel_to_inn():
    player["checkpoint"] = "chapter_one_scene_2_Inn"
    perform_save()
    clear_screen()
    time.sleep(0.5)
    typewriter("As you walk into the town exhausted you come across and INN that appears to be open")
    time.sleep(0.5)


def travel_to_tavern():
    player["checkpoint"] = "chapter_one_scene_2_tavern"
    perform_save()
    clear_screen()
    time.sleep(0.5)
    typewriter("As you walk towards what looks to be the Tavern of the village you notice, a few people gathered around near the entrance.\nAbove the door you see a brown haired woman leaning out the window.")
    time.sleep(0.3)
    typewriter("You hear shouting as you approach")
    time.sleep(1)
    clear_screen()
    print_speaker("Shouting Woman (From upper floor window)")
    typewriter("I already told you to get the hell out of here, I've gotta open this place up in a few hours\nand I also wouldn't mind just getting a little more sleep! ")
    time.sleep(0.5)
    print_speaker("Shouting Man")
    typewriter("You piece of shit! I know you were in on it with that guy at the bar, you can't fool me! ")
    time.sleep(0.5)
    print_speaker("Shouting Woman")
    typewriter("Don't blame your poor playing skills on me")
    time.sleep(0.5)
    print_speaker("Shouting Man")
    typewriter("You know what, I'll be back, just you wait, i'm coming for you, that man, and my damn money")
    time.sleep(0.5)
    print_speaker("Shouting Woman")
    typewriter("Yeah, I'm sure you will.")
    time.sleep(0.5)
    typewriter("I've had enough of this shit, I'm going back to sleep, Tavern opens in 3 hours now because of this fool")
    time.sleep(2)
    clear_screen()
    typewriter("After witnessning that argument unfold in front of you, you hear an unfamiliar voice coming from behind you")
    time.sleep(0.5)
    print_speaker("Villager")
    typewriter("I've never seen you around here before, we get vistors from time to time, but they usually don't look\nlike they've been though whatever Hell you've been through")
    time.sleep(3)
    clear_screen()
    time.sleep(0.5)
    typewriter("You look down and realize your clothes show sign of burns that could have been only cooled by the Icy winds from the moutains you traveld from")
    time.sleep(0.5)

    # ───────────────────────────────────────────────
    # Chapter 1: Scene 2: Dialouge 1
    # ───────────────────────────────────────────────
    print_speaker("Villager")
    typewriter("So I can't help but ask but..what the hell happened to you?")
    
    print("a) Tell him you're not sure what happened to you")
    print("b) Tell him about your meeting with Viirish")

    # Hidden option based on Intelligence
    if player["stats"]["intelligence"] >= 6:
        print("c) Explain you were on a camping trip that didn't go well. (Intelligence Requirement met: 6)")
    choice = get_choice(["a", "b", "c"] if player["stats"]["intelligence"] >= 6 else ["a", "b"])

    if choice == "a":
        print_speaker("Villager")
        typewriter("Strange...")
        time.sleep(0.3)
        typewriter("But I'm not judging, I've definetly had my days of waking up in the woods drunk off my ass so I get you")
        time.sleep(0.3)
        clear_screen()
        time.sleep(0.3)
    elif choice == "b":
        time.sleep(0.3)
        print_speaker("Villager")
        typewriter("Viirish? I can't say that name has too much meaning to me, but I have read ")
        time.sleep(0.3)
        typewriter("Alderos has watched over us since I was born though")
        time.sleep(0.3)
        typewriter("You definetly might not want to mention that name around here, I was only just being born at the time\nbut there are some people around here old enough to remember those days")
        time.sleep(0.3)
        clear_screen()
        time.sleep(0.3)
    elif choice == "c":
        print("")
        typewriter("You tell him what little you know — the fortress, the cold, the voice.")

    # ───────────────────────────────────────────────
    # Chapter 1: Scene 2: Dialouge 1
    # ───────────────────────────────────────────────
    print_speaker("Villager")
    typewriter("Name's Peter, what should I call you?")
    time.sleep(2)
    typewriter("You")
    time.sleep(0.3)
    name = player["name"] or "stranger"
    typewriter(f"{name}...My name is {name}'")
    time.sleep(0.3)
    print_speaker("Peter")
    typewriter(f"Well good to meet you {name}.")
    time.sleep(0.3)
    typewriter("I'm assuming you probably haven't eatin in a while either, if you want we can head inside the tavern")
    time.sleep(0.3)
    typewriter("My older sister Erena owns the place so we kinda have free reign there. I'll introduce you")
    time.sleep(5)
    clear_screen()
    typewriter("You and Peter walk into the tavern and walk toward the kitchen")
    time.sleep(0.5)
    #Rewrite this and add more visual description to ground the user in the environment
    











# Game Narrative Start
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# Scene 1: 
# - 
# - Potential Skill Gains
#   - +1 INT
#   - +2 STR
# ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────    
def Chapter_one_start():
    player["checkpoint"] = "chapter_one"
    perform_save()
    clear_screen()
    time.sleep(0.3)
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
    switch_music("audio/chapter_two_theme.mp3", fadeout_time=2000)
    player["checkpoint"] = "chapter_one_scene_2"
    perform_save()
    typewriter("You approach the village just as sun begins to peek above the sun.")
    time.sleep(0.5)

    print("a) travel to the Inn")
    print("b) travel to the Tavern")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b", "c"])

    if choice == "a":
        travel_to_inn()
    elif choice == "b":
        travel_to_tavern()


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