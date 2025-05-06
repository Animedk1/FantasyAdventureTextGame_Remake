import time
import sys
import os
import pygame
import random
import state 
import textwrap

# ───────────────────────────────────────────────
# SYSTEM UTILITIES
# ───────────────────────────────────────────────

pygame.mixer.init()

#Add the skill gain sound
skill_gain_sound = pygame.mixer.Sound("audio/skill_gain.wav")
skill_gain_sound.set_volume(0.8)  # optional

#Play Skill Gain sound
def play_skill_gain_sound():
    skill_gain_sound.play()


# Load background music
pygame.mixer.music.load("audio/bgmusic_prologue.mp3")  # ← Replace with your actual music file
pygame.mixer.music.set_volume(0.9)

if state.musicOn:
    pygame.mixer.music.play(-1)  # Loop forever

import pygame
import state

# Assume pygame.mixer.init() has already been called earlier
checkpoint_music_map = {
    "intro": {
        "file": "audio/bgmusic_prologue.mp3",
        "volume": 0.8
    },
    "chapter_one": {
        "file": "audio/bgmusic_prologue.mp3",
        "volume": 0.8
    },
    "chapter_one_scene_2": {
        "file": "audio/bgmusic_village.mp3",
        "volume": 0.3
    },
    "chapter_one_scene_2_Inn": {
        "file": "audio/bgmusic_village.mp3",
        "volume": 0.3
    },
    "chapter_one_scene_2_tavern": {
        "file": "audio/bgmusic_village.mp3",
        "volume": 0.3
    }
}

def switch_music(checkpoint, fadeout_time=1000):
    if not state.musicOn:
        return  # User disabled music

    track_info = checkpoint_music_map.get(checkpoint)

    if track_info:
        try:
            pygame.mixer.music.fadeout(fadeout_time)  # Fade out over 1 second
            pygame.mixer.music.load(track_info["file"])
            pygame.mixer.music.set_volume(track_info["volume"])
            pygame.mixer.music.play(-1)  # Loop indefinitely
        except Exception as e:
            print(f"Error switching music for checkpoint {checkpoint}: {e}")



# Load typing sounds
typing_sounds = [
    pygame.mixer.Sound("audio/click1.wav"),
    pygame.mixer.Sound("audio/click2.wav"),
    pygame.mixer.Sound("audio/click3.wav"),
    pygame.mixer.Sound("audio/click4.wav"),
    pygame.mixer.Sound("audio/click5.wav"),
]

def typewriter(text, delay=0.05, speaker=None):
    if text.strip():
        if speaker:
            state.dialogue_log.append(f"{speaker}:\n{text}")
        else:
            state.dialogue_log.append(f"Narrator:\n{text}")


    #typewriter Effecct
    for char in text:
        if state.soundOP:
            sound = random.choice(typing_sounds)
            sound.play()
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def flush_input():
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

def safe_input(prompt="→ ", pause_time=0.1):
    time.sleep(pause_time)
    flush_input()
    return input(prompt)

def toggle_music(on: bool):
    state.musicOn = on
    if on:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
        
# ───────────────────────────────────────────────
# SPEAKER FORMATTER
# ───────────────────────────────────────────────

def print_speaker(name, mood=None):
    if mood:
        print(f"\n>> \u001b[1m{name} ({mood})\u001b[0m <<")
    else:
        print(f"\n>> \u001b[1m{name}\u001b[0m <<")


# ───────────────────────────────────────────────
# DEFAULT DISPLAY FUNCTIONS
# ───────────────────────────────────────────────

def show_stats():
    typewriter(f"\nName: {state.player['name'] or 'Unknown'}")
    typewriter(f"Gold: {state.player['gold']}")
    typewriter(f"Armored: {'Yes' if state.player['armored'] else 'No'}")

    typewriter("\nStats:")
    for stat, value in state.player["stats"].items():
        typewriter(f"  {stat.title()}: {value}")

    met_anyone = state.game_state.get("erena_met") or state.game_state.get("markus_met")
    if met_anyone:
        typewriter("\nRelationships:")
        if state.game_state.get("erena_met"):
            typewriter(f"  Erena: {state.player['relationships'].get('Erena', 0)}")
        if state.game_state.get("markus_met"):
            typewriter(f"  Markus: {state.player['relationships'].get('Markus', 0)}")

def show_inventory():
    if state.player["inventory"]:
        typewriter("\nYou're carrying:")
        for item in state.player["inventory"]:
            typewriter(f"- {item}")
    else:
        typewriter("\nYour inventory is empty.")

# ───────────────────────────────────────────────
# INPUT HANDLER (with command support)
# ───────────────────────────────────────────────

def get_choice(valid_choices):
    from backend import save_game, load_game, delete_save

    while True:
        choice = safe_input().lower()

        if choice == "help":
            print("\u001b[33mAvailable Commands:\u001b[0m")
            print("  \u001b[1mlog\u001b[0m       - Review the last few lines of dialogue")
            print("  \u001b[1mstats\u001b[0m     - View your character stats and relationships")
            print("  \u001b[1minventory\u001b[0m - See what items you're carrying")
            print("  \u001b[1mgold\u001b[0m      - Check how much gold you have")
            print("  \u001b[1msound on\u001b[0m    - Enable typewriter sound effects")
            print("  \u001b[1msound off\u001b[0m   - Disable typewriter sound effects")
            print("  \u001b[1mmusic on\u001b[0m    - Play background music")
            print("  \u001b[1mmusic off\u001b[0m   - Stop background music")
            print("  \u001b[1msave\u001b[0m      - Save your current progress")
            print("  \u001b[1mload\u001b[0m      - Load your last saved game")
            print("  \u001b[1mrestart\u001b[0m   - Delete your save and start fresh")
            print("  \u001b[1mexit\u001b[0m      - Exit the game")
            continue

        if choice == "exit":
            typewriter("You've chosen to exit. You'll return soon.")
            sys.exit()
        elif choice == "stats":
            show_stats()
        elif choice == "inventory":
            show_inventory()
        elif choice == "gold":
            print(f"\nYou currently have {state.player['gold']} gold.\n")
        elif choice == "save":
            save_game()
        elif choice == "load":
            load_game()
        elif choice in ["restart", "delete"]:
            delete_save()
        elif choice == "sound on":
            state.soundOP = True
            typewriter("Typewriter sound has been turned ON.")
        elif choice == "sound off":
            state.soundOP = False
            typewriter("Typewriter sound has been turned OFF.")
        elif choice == "music on":
            toggle_music(True)
            typewriter("Background music is now playing.")
        elif choice == "music off":
            toggle_music(False)
            typewriter("Background music has been stopped.")
        elif choice in valid_choices:
            return choice
        elif choice in ["log", "history"]:
            print("\n\u001b[36m--- Recent Dialogue ---\u001b[0m")
            for entry in state.dialogue_log:
                print(entry)
                print()  # adds blank line between entries
            print("\n(Type your choice again below.)")


        else:
            typewriter("Invalid choice. Try again.")

# ───────────────────────────────────────────────
# Game Over Function
# ───────────────────────────────────────────────

def game_over():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\u001b[31m==== GAME OVER ====\u001b[0m\n")
    time.sleep(1)

    # Player Summary
    print("\nFinal Stats:")
    for stat, value in state.player["stats"].items():
        print(f"  {stat.title()}: {value}")

    # Inventory
    if state.player["inventory"]:
        print("\nInventory:")
        for item in state.player["inventory"]:
            print(f"  - {item}")
    else:
        print("\nInventory: Empty")

    # Relationships
    met_anyone = state.game_state.get("erena_met") or state.game_state.get("markus_met")
    if met_anyone:
        print("\nRelationships:")
        if state.game_state.get("erena_met"):
            print(f"  Erena: {state.player['relationships'].get('Erena', 0)}")
        if state.game_state.get("markus_met"):
            print(f"  Markus: {state.player['relationships'].get('Markus', 0)}")

    # Key Choices (if tracked)
    print("\nMajor Choices & Events:")
    if state.game_state.get("met_mysterious_voice"):
        print("- Encountered the Mysterious Voice")
    if state.player["armored"]:
        print("- Chose to wear the cursed armor")
    else:
        print("- Did not wear the armor")
    if "Eldrich Plate Armour" in state.player["inventory"]:
        print("- Found the Eldrich Plate Armour")

    print("\nThank you for playing.\n")
    time.sleep(2)

    print("\nWould you like to return to the main menu?")
    print("a) Restart Game")
    print("b) Exit")

    while True:
        choice = input("→ ").lower()
        if choice in ["a", "restart"]:
            from backend import startMenu
            startMenu()
            break
        elif choice in ["b", "exit"]:
            sys.exit()
        else:
            print("Please choose a valid option.")

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# Perform Save - a workaround to avoid the circular import caused by importing save_game from backend into the chapter files
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def perform_save():
    """
    Safe wrapper to trigger save_game from backend without causing circular import issues.
    """
    try:
        from backend import save_game
        save_game()
    except Exception as e:
        typewriter(f"An error occurred while saving the game: {e}")

# ─────────────────────────────────────────────────────────────────────────────────────────────
# Say Function - combines print_speaker and typewriter for cleaner code
# ─────────────────────────────────────────────────────────────────────────────────────────────

def say(text, speaker=None):
    # Determine label and log name
    if speaker:
        label = f"\u001b[33m{speaker}:\u001b[0m"  # Yellow for characters
        log_name = f"\u001b[33m{speaker}:\u001b[0m"
    else:
        label = "\u001b[35mNarrator:\u001b[0m"    # Purple for narrator
        log_name = f"\u001b[35mNarrator:\u001b[0m"

    # Print to screen
    print(f"\n{label}")
    typewriter(text)

    # Prepare single-line log entry with color
    collapsed_text = text.replace("\n", " ").strip()
    log_entry = f"{log_name} {collapsed_text}\n"

    state.dialogue_log.append(log_entry)

    if len(state.dialogue_log) > 30:
        state.dialogue_log.pop(0)

def show_log():
    print("\n\u001b[36m--- Dialogue Log ---\u001b[0m\n")
    for entry in state.dialogue_log:
        print(entry)
        print()  # Adds a blank line between each entry
