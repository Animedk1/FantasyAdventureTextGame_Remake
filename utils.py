import time
import sys
import os
import pygame
import random
import state
import colorama
from pathlib import Path

# Ensure ANSI color codes display properly on Windows
colorama.init()

# ───────────────────────────────────────────────
# AUDIO SETUP
# ───────────────────────────────────────────────

pygame.mixer.init()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = Path(sys._MEIPASS)  # Used by PyInstaller
    except AttributeError:
        base_path = Path(__file__).parent
    return base_path / relative_path

# Skill gain sound
skill_gain_sound = pygame.mixer.Sound(str(resource_path("audio/skill_gain.wav")))
skill_gain_sound.set_volume(0.8)

def play_skill_gain_sound():
    skill_gain_sound.play()

# Initial background music
pygame.mixer.music.load(str(resource_path("audio/bgmusic_prologue.mp3")))
pygame.mixer.music.set_volume(0.9)
if state.musicOn:
    pygame.mixer.music.play(-1)

# Background music map
checkpoint_music_map = {
    "intro": {"file": "audio/bgmusic_prologue.mp3", "volume": 0.8},
    "chapter_one": {"file": "audio/bgmusic_prologue.mp3", "volume": 0.8},
    "chapter_one_scene_2": {"file": "audio/bgmusic_village.mp3", "volume": 0.3},
    "chapter_one_scene_2_Inn": {"file": "audio/bgmusic_village.mp3", "volume": 0.3},
    "chapter_one_scene_2_tavern": {"file": "audio/bgmusic_village.mp3", "volume": 0.3}
}

def switch_music(checkpoint, fadeout_time=1000):
    if not state.musicOn:
        return
    track_info = checkpoint_music_map.get(checkpoint)
    if track_info:
        try:
            pygame.mixer.music.fadeout(fadeout_time)
            music_file = resource_path(track_info["file"])
            pygame.mixer.music.load(str(music_file))
            pygame.mixer.music.set_volume(track_info["volume"])
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error switching music for checkpoint {checkpoint}: {e}")

# Typing sounds
typing_sounds = [
    pygame.mixer.Sound(str(resource_path(f"audio/click{i}.wav"))) for i in range(1, 6)
]

def typewriter(text, delay=0.05, speaker=None):
    if text.strip():
        if speaker:
            state.dialogue_log.append(f"{speaker}:\n{text}")
        else:
            state.dialogue_log.append(f"Narrator:\n{text}")
    for char in text:
        if state.soundOP:
            random.choice(typing_sounds).play()
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

# ───────────────────────────────────────────────
# GENERAL UTILITIES
# ───────────────────────────────────────────────

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
# DISPLAY HELPERS
# ───────────────────────────────────────────────

def print_speaker(name, mood=None):
    if mood:
        print(f"\n>> \u001b[1m{name} ({mood})\u001b[0m <<")
    else:
        print(f"\n>> \u001b[1m{name}\u001b[0m <<")

def show_stats():
    typewriter(f"\nName: {state.player['name'] or 'Unknown'}")
    typewriter(f"Gold: {state.player['gold']}")
    typewriter(f"Armored: {'Yes' if state.player['armored'] else 'No'}")
    typewriter("\nStats:")
    for stat, value in state.player["stats"].items():
        typewriter(f"  {stat.title()}: {value}")
    if state.game_state.get("erena_met") or state.game_state.get("markus_met"):
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
# GAME INTERACTION
# ───────────────────────────────────────────────

def get_choice(valid_choices):
    from backend import save_game, load_game, delete_save
    while True:
        choice = safe_input().lower()
        if choice == "help":
            print("\u001b[33mAvailable Commands:\u001b[0m")
            print("  log, stats, inventory, gold, sound on/off, music on/off, save, load, restart, exit")
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
            show_log()
            print("\n\u001b[90m(Showing previous dialogue... returning to choice in 5 seconds.)\u001b[0m")
            time.sleep(5)

            if state.last_prompt:
                print(f"\n\u001b[35m{state.last_prompt}\u001b[0m")  # Colored reprint of the last prompt

            print("\n\u001b[32mPlease make your choice again:\u001b[0m")


def game_over():
    clear_screen()
    print("\n\u001b[31m==== GAME OVER ====\u001b[0m\n")
    time.sleep(1)
    print("\nFinal Stats:")
    for stat, value in state.player["stats"].items():
        print(f"  {stat.title()}: {value}")
    print("\nInventory:")
    for item in state.player["inventory"] or ["Empty"]:
        print(f"  - {item}")
    if state.game_state.get("erena_met") or state.game_state.get("markus_met"):
        print("\nRelationships:")
        if state.game_state.get("erena_met"):
            print(f"  Erena: {state.player['relationships'].get('Erena', 0)}")
        if state.game_state.get("markus_met"):
            print(f"  Markus: {state.player['relationships'].get('Markus', 0)}")
    print("\nMajor Choices & Events:")
    if state.game_state.get("met_mysterious_voice"):
        print("- Encountered the Mysterious Voice")
    print("- Chose to wear the cursed armor" if state.player["armored"] else "- Did not wear the armor")
    if "Eldrich Plate Armour" in state.player["inventory"]:
        print("- Found the Eldrich Plate Armour")
    print("\nThank you for playing.\n")
    time.sleep(2)
    print("a) Restart Game\nb) Exit")
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

# ───────────────────────────────────────────────
# DIALOGUE / LOGGING
# ───────────────────────────────────────────────

def say(text, speaker=None):
    label = f"\u001b[33m{speaker}:\u001b[0m" if speaker else "\u001b[35mNarrator:\u001b[0m"
    log_name = label
    print(f"\n{label}")
    typewriter(text)
    entry = f"{log_name} {text.replace(chr(10), ' ')}\n"
    state.dialogue_log.append(entry)
    if len(state.dialogue_log) > 30:
        state.dialogue_log.pop(0)

def show_log():
    print("\n\u001b[36m--- Dialogue Log ---\u001b[0m\n")
    for entry in state.dialogue_log:
        print(entry)
        print()

# ───────────────────────────────────────────────
# SAVE WRAPPER
# ───────────────────────────────────────────────

def perform_save():
    try:
        from backend import save_game
        save_game()
    except Exception as e:
        typewriter(f"An error occurred while saving the game: {e}")
