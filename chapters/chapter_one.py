import time
import state
from utils import typewriter, clear_screen, get_choice, say
from engine import unarmored_event
from utils import play_skill_gain_sound, print_speaker, perform_save,switch_music,say_with_pauses
from combat.enemies import create_shouting_man
from combat.battle_system import start_battle
from combat.battle_scenarios import Peter_battle_tutorial


# ───────────────────────────────────────────────
# Choice (1) functions
# Notes:
#   - All three option lead you to talking with the sword
# ───────────────────────────────────────────────

def check_sword():
    clear_screen()

    # Intro sequence with environmental change
    say_with_pauses([
        "As you reach out to grab the sword from the snow, you feel a sharp pain in your chest.",
        "The sensation is so strong it brings you to your knees.",
        "As you look up from staring down at the ground you realize the feeling of the bitter cold has dissipated...",
        "The world in front of you has changed.",
        "A blood red hue covers the sky and you find yourself standing atop a tower built of a dark unknown material.",
        "Behind you is a sealed door.",
        "Before you can bring yourself to investigate you hear a powerful forboding voice coming from the sky.",
        "You try to collect yourself, but find that you are unable to move."
    ], delay=0.5)

    time.sleep(4)
    clear_screen()
    state.game_state["met_mysterious_voice"] = True
    time.sleep(1)

    # Mysterious Voice monologue
    say_with_pauses([
        "Your time is short here, so listen.",
        "You will understand with time, but you are not the first to have been gifted with my power.",
        "We shall hope you will be the last.",
        "A plague has spread throughout the isles from which you hail. So far as to reach within my domain.",
        "The isles must burn and you need to be the one to ignite the flame.",
        "Take the sword I've given you to the capital city of Aedros.",
        "You are not my only choice, but you are important. If you value your life and the lives of those you will soon meet, I caution you to take this task seriously."
    ], speaker="Mysterious Voice", delay=1)

    time.sleep(4)
    clear_screen()

    say("Do not disappoint me by being as disposable as the rest.", speaker="Mysterious Voice")
    time.sleep(4)

    clear_screen()

    # Back to the world
    say_with_pauses([
        "The world around you fades and you find yourself back in the snowy environment you were in before.",
        "The pain you previously felt has subsided and you now have full control of your body.",
        "-- something shows you the way to the village.",
        "You prepare to set off on the path to the village that was shown to you."
    ], delay=0.5)


def equip_armour():
    clear_screen()

    say_with_pauses([
        "You grab the armour from the snow.",
        "Upon closer inspection, you realize you've never seen armor made of this material.",
        "When placing the armour on your body, you're met with a feeling of dread; a burning sensation courses through you.",
        "The armor begins to dissipate within your skin and a red symbol is burned into the palm of your hand.",
        "Although the armor isn't visible, you can still feel its protection"
    ], delay=0.3)

    state.player["armored"] = True
    state.player["inventory"].append("Eldrich Plate Armour")

    check_sword()


def equip_armour_after_Sword():
    clear_screen()

    say_with_pauses([
        "You grab the armour from the snow.",
        "Upon closer inspection, you realize you've never seen armor made of this material.",
        "When placing the armour on your body, you're met with a feeling of dread; a burning sensation courses through you.",
        "The armor begins to dissipate within your skin and a red symbol is burned into the palm of your hand.",
        "Although the armor isn't visible, you can still feel its protection"
    ], delay=0.3)

    state.player["armored"] = True
    state.player["inventory"].append("Eldrich Plate Armour")



def check_fire():
    clear_screen()

    say_with_pauses([
        "You lean down and check the fire.",
        "It's too far gone. The embers are cold and dead.",
        "After inspecting the fire, you see the snow is covering the remains of what looks like was once a campsite.",
        "Upon further inspection, you can tell this place was abandoned some time ago...though exactly how long, you can't quite tell."
    ], delay=0.5)

    # Notification Sound
    play_skill_gain_sound()
    say("(+1 intelligence)")
    state.player["stats"]["intelligence"] += 1

    say_with_pauses([
        "While taking in the environment around you, you hear a faint noise that echoes that of a whisper.",
        "Upon further inspection, you notice it's the sword."
    ], delay=0.5)

    time.sleep(1)
    check_sword()


def equip_armor_scene_1():
    say("You look down at the armor laying in the snow and think about your next move...")
    print("a) Equip the armour")
    print("b) Continue without it")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b"])

    if choice == "a":
        equip_armour_after_Sword()
        state.player["armored"] = True
        state.player["inventory"].append("Eldrich Plate Armour")
    elif choice == "b":
        say("You've chosen to leave the armor behind")


# ───────────────────────────────────────────────
# Choice (2) functions
# ───────────────────────────────────────────────
def travel_to_inn():
    state.player["checkpoint"] = "chapter_one_scene_2_Inn"
    perform_save()
    clear_screen()

    say_with_pauses([
        "As you wearily walk into the town, you come across an inn that appears to be open.",
        "You walk in to find the place empty, but there are signs that someone is here.",
        "Just as you move to rest in a nearby chair, you hear a loud boom coming from a room nearby.",
        "You jump up vigilantly and make your way to the doorway of the other room."
    ], delay=0.5)

    time.sleep(4)
    clear_screen()

    say("Ah man, the old man's going to kill me for this", speaker="Disappointed Man")
    time.sleep(0.5)
    say("As you approach the doorway, you step on a loose floor board nearby.")
    time.sleep(1)
    say("The man quickly turns around to inspect the noise behind him.")
    time.sleep(4)

    say(
        "Oh hello friend, I didn't hear you come in. We typically don't have too much activity around these hours "
        "so I can't say I was paying too much attention.\n"
        "What should I call you?",
        speaker="Disappointed Man"
    )
    time.sleep(0.5)

    say("You struggle for a moment, but somehow remember your name.")
    
    # Pulls player name from state
    name = state.player["name"] or "stranger"
    say(f"{name}...My name is {name}'", speaker=f"{name}")
    time.sleep(0.5)

    say(f"Well {name} it's a good thing you came when you did. Name's Markus", speaker="Disappointed Man")
    time.sleep(0.5)

    say("You probably already heard, but I have a bit of a situation here.")

    
    

def travel_to_tavern():
    state.player["checkpoint"] = "chapter_one_scene_2_tavern"
    perform_save()
    clear_screen()

    say_with_pauses([
        "As you walk towards what appears to be the tavern of the village, you notice a few people gathered near the entrance.",
        "Above the door, you see a brown haired woman leaning out the window.",
        "You hear shouting as you approach"
    ], delay=0.5)

    time.sleep(5)
    clear_screen()

    # Argument between NPCs
    say("I already told you to get the hell out of here, I've gotta open this place up in a few hours\nand I also wouldn't mind just getting a little more sleep!", speaker="Shouting Woman (From upper floor window)")
    time.sleep(0.5)
    say("You piece of shit! I knew you were in on it with that guy at the bar, you can't fool me!", speaker="Shouting Man")
    time.sleep(0.5)
    say("Don't blame your poor playing skills on me!", speaker="Shouting Woman")
    time.sleep(0.5)
    say("You know what? I'll be back, just you wait- I'm coming for you, that man, and my damn money", speaker="Shouting Man")
    time.sleep(0.5)
    say_with_pauses([
        "Yeah, I'm sure you will.",
        "I've had enough of this shit- I'm going back to sleep. The tavern opens in three hours now because of this fool",
        ],speaker="Shouting Woman", delay=0.5)

    time.sleep(5)
    clear_screen()

    say("After witnessing the argument unfold in front of you, you hear an unfamiliar voice coming from behind you")
    time.sleep(0.5)

    say("I've never seen you around here before; we get visitors from time to time, but they usually don't look\nlike they've been through whatever the hell you've been through", speaker="Villager")
    time.sleep(5)

    clear_screen()
    time.sleep(0.5)

    say("You look down and realize your clothes show signs of burns that could have been only cooled by the icy winds from the mountains you traveled from.")

    # ───────────────────────────────────────────────
    # Chapter 1: Scene 2: Dialogue 1 Choice
    # ───────────────────────────────────────────────
    say("So, I can't help but ask...what the hell happened to you?", speaker="Villager")

    print("a) Tell him you're not sure what happened to you")
    print("b) Tell him about your meeting with Viirish")

    # Save Prompt
    state.last_prompt = (
        "So, I can't help but ask...what the hell happened to you?\n\n"
        "a) Tell him you're not sure what happened to you\n"
        "b) Tell him about your meeting with Viirish"
    )

    # Hidden option based on Intelligence
    if state.player["stats"]["intelligence"] >= 6:
        print("c) Explain you were on a camping trip that didn't go well. (Intelligence Requirement met: 6)")

    choice = get_choice(["a", "b", "c"] if state.player["stats"]["intelligence"] >= 6 else ["a", "b"])

    if choice == "a":
        say("Strange...", speaker="Villager")
        time.sleep(0.3)
        say("But I'm not judging, I've definitely had my days of waking up in the woods drunk off my ass, so I get you", speaker="Villager")
        time.sleep(5)
        clear_screen()
        time.sleep(0.3)

    elif choice == "b":
        time.sleep(0.3)
        say("Viirish? I can't say that name has too much meaning to me, but I have read", speaker="Villager")
        time.sleep(0.3)
        say("Alderos has watched over us since I was born though", speaker="Villager")
        time.sleep(0.3)
        say("You might not want to mention that name around here; I was only born at the time\nbut there are some people around here old enough to remember those days", speaker="Villager")
        time.sleep(5)
        clear_screen()
        time.sleep(0.3)

    elif choice == "c":
        say("You tell him what little you know — the fortress, the cold, the voice.")

    # Continue Scene
    say("Name's Peter, what should I call you?", speaker="Villager")
    time.sleep(2)
    say("You scramble to remember your name.")
    time.sleep(0.3)

    name = state.player["name"] or "stranger"
    say(f"{name}...My name is {name}'", speaker=f"{name}")
    time.sleep(0.3)

    say(f"Well, good to meet you {name}.", speaker="Peter")
    time.sleep(0.3)
    say("I'm assuming you haven't eaten in a while either. If you want, we can head inside the tavern", speaker="Peter")
    time.sleep(0.3)
    say("My older sister Erena owns the place, so we have free reign there. I'll introduce you", speaker="Peter")
    time.sleep(5)

    clear_screen()
    say("You and Peter walk into the tavern and walk towards the kitchen")
    time.sleep(0.5)

    # Rewrite note preserved
    say("The place looks a bit rundown, but the decor adds a warm charm to it.\nAlong the walls you see paintings of what appears to be some sort of deity\nYou walk over with Peter to take a seat at the bar.")
    time.sleep(0.5)

    say_with_pauses([
        "ERENA! (Peter Shouts)",
        "Guess she wasn't kidding about going back to sleep. Which means..",
        "bar's all ours!"
    ], speaker="Peter", delay=0.5)  

    time.sleep(0.5)

    say("Peter excitedly jumps out of his seat.")

    time.sleep(0.5)
    
    say_with_pauses([
        "But before we start drinking-because trust me, you look like you need one more than me-",
        "I can't help but notice that sword on your back. It's unlike anything I've ever seen around here",
        "You must be really good at sword fighting to be carrying something like that",
        "I've been practicing a bit myself, so let's say we put a bit of a wager on this",
        "If you win.... but if I win.....",
        "What do you say: are you up for it?"
    ], speaker="Peter", delay=0.5)         
    
    time.sleep(0.5)

    #Add a save game and a checkpoint here:


    # ───────────────────────────────────────────────
    # Chapter 1: Practice Battle 1: Peter
    # ───────────────────────────────────────────────

    say("Would you like to try the tutorial fight?")

    print("a) Sure!")
    print("b) Not this time")

    # Save Prompt
    state.last_prompt = (
        "Would you like to try the tutorial fight?\n\n"
        "a) Sure!\n"
        "b) Not this time"
    )

    choice = get_choice(["a", "b", "c"] if state.player["stats"]["intelligence"] >= 6 else ["a", "b"])

    if choice == "a":
        say_with_pauses([
            "See, I knew I liked you!",
            "Oh, before I forget: drink this. I need you at full strength for this.",
        ], speaker="Peter", delay=0.5)    
        time.sleep(5)
        clear_screen()
        time.sleep(0.3)
        #Temporary
        perform_save()
        state.player["checkpoint"] = "Peter Tutorial battle"
        Peter_battle_tutorial()

    elif choice == "b":
        say_with_pauses([
            "See, I knew I liked you!",
            "Oh, before I forget: drink this. I need you at full strength for this.",
        ], speaker="Peter", delay=0.5)    
        time.sleep(5)
        clear_screen()


    # ───────────────────────────────────────────────
    # Chapter 1: Battle 1
    # ───────────────────────────────────────────────

    #Save Game  - Pre-combat checkpoint:
    perform_save()
    state.player["checkpoint"] = "chapter_one_battle_1"
    

    #Start Battle
    enemy = create_shouting_man()
    start_battle(enemy, reward_gold=15, reward_item="Health Potion")
    

    say("Test String")












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
    state.player["checkpoint"] = "chapter_one"
    perform_save()
    clear_screen()
    time.sleep(0.3)

    say("Prologue: Awakening")
    time.sleep(4)
    clear_screen()

    say_with_pauses([
        "You wake up sitting in front of the ashes of a recently lit campfire.",
        "Your memory is hazy.",
        "Your back is pressed against a cold stone wall that once belonged to a small fortress within the land.",
        "Beside you lies your armour, in need of repair. Beside it is a sword with a faint red glow, buried in snow.",
        "You look toward the sky.",
        "A crimson moon sinks slowly behind the trees. Daylight is near, but the night is still bitter.",
        "You stand up and consider your next move...\n"
    ], delay=0.5)

    # Stores last prompt for log
    state.last_prompt = (
        "You stand up and consider your next move...\n"
        "\n"
        "a) Equip your armour\n"
        "b) Inspect the small camp around you\n"
        "c) Inspect the sword beneath the snow\n"
        "(Type 'help' for command list)"
    )

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
    if not state.player["armored"]:
        equip_armor_scene_1()

    # ───────────────────────────────────────────────
    # Bonus Encounter if not armored
    # ───────────────────────────────────────────────
    if not state.player["armored"]:
        unarmored_event()

    # Start of Scene 2
    chapter_one_scene2()



def chapter_one_scene2():
    switch_music("chapter_one_scene_2", fadeout_time=2000)
    state.player["checkpoint"] = "chapter_one_scene_2"
    perform_save()

    say("You approach the village just as the sun begins to peek above the mountains.")
    time.sleep(0.5)

    # Save prompt for dialogue log
    state.last_prompt = (
        "You approach the village just as the sun begins to peek above the mountains.\n\n"
        "a) travel to the Inn\n"
        "b) travel to the Tavern\n"
        "(Type 'help' for command list)"
    )

    print("a) travel to the Inn")
    print("b) travel to the Tavern")
    print("(Type 'help' for command list)")

    choice = get_choice(["a", "b"])

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