import os
import json
import time
import state
from utils import typewriter, clear_screen, safe_input, switch_music, checkpoint_music_map
from chapters.chapter_one import Chapter_one_start, chapter_one_scene2,travel_to_inn,travel_to_tavern
from combat.battle_scenarios import Peter_battle_tutorial
#from config import DEV_MODE


# ───────────────────────────────────────────────
# SAVE / LOAD SYSTEM
# ───────────────────────────────────────────────

def get_save_path():
    documents = os.path.expanduser("~/Documents")
    save_dir = os.path.join(documents, "FantasyTextAdventureSaves")
    os.makedirs(save_dir, exist_ok=True)
    return os.path.join(save_dir, "savefile.json")

def save_game():
    try:
        save_data = {"player": state.player, "game_state": state.game_state}
        with open(get_save_path(), "w") as f:
            json.dump(save_data, f)
        typewriter("\nGame saved successfully!\n")
    except Exception as e:
        typewriter(f"\nFailed to save game: {e}")

def load_game():
    try:
        with open(get_save_path(), "r") as f:
            save_data = json.load(f)

            # Update in-place to preserve references
            state.player.clear()
            state.player.update(save_data.get("player", {}))

            state.game_state.clear()
            state.game_state.update(save_data.get("game_state", {}))
 
        typewriter("\nGame loaded successfully!\n")
        time.sleep(1)
        clear_screen()
        resume_checkpoint(state.player.get("checkpoint", "intro"))
    except FileNotFoundError:
        typewriter("\nNo save file found.\n")
    except Exception as e:
        typewriter(f"\nFailed to load game: {e}")

def delete_save():
    try:
        os.remove(get_save_path())
        typewriter("You've chosen a new path.\nFine by me, the outcome will remain the same.")
    except FileNotFoundError:
        typewriter("No save file found to delete.")

def resume_checkpoint(point):
    # Set music based on checkpoint
    switch_music(point)

    #Resume Story Based on checkpoint
    if point == "intro":
        gameIntro()
    elif point == "chapter_one":
        Chapter_one_start()
    elif point == "chapter_one_scene_2":
        chapter_one_scene2()
    elif point == "chapter_one_scene_2_Inn":
        travel_to_inn()
    elif point == "chapter_one_scene_2_tavern":
        travel_to_tavern()
    elif point == "chapter_one_battle_1":
        travel_to_tavern() # Create a fucntiont that contains the battle so the player can resume for before the fight
    elif point == "Peter Tutorial battle":
        Peter_battle_tutorial()
        
    
    else:
        typewriter("Unknown checkpoint. Starting from the beginning...")
        gameIntro()

# ───────────────────────────────────────────────
# GAME FLOW
# ───────────────────────────────────────────────

def startMenu():
    clear_screen()
    save_path = get_save_path()

    if os.path.exists(save_path):
        try:
            with open(save_path, "r") as f:
                saved_data = json.load(f)
                saved_name = saved_data.get("player", {}).get("name", "traveler") or "traveler"
        except:
            saved_name = "traveler"

        typewriter("You seem familiar...")
        time.sleep(1)
        typewriter(f"Ah, I remember you, {saved_name}...")
        time.sleep(1)
        typewriter("Will you continue to finish the work you've started?\n")

        print("a) Load Game")
        print("b) Start New Game\n")

        while True:
            choice = safe_input("→ ").lower()
            if choice in ["a", "load", "1"]:
                load_game()
                break
            elif choice in ["b", "new", "2"]:
                delete_save()
                clear_screen()
                gameIntro()
                break
            else:
                typewriter("Please choose a valid option.")
    else:
        gameIntro()

def gameIntro():
    state.player["checkpoint"] = "intro"
    typewriter("Your Journey begins here, but before you venture forth...")
    time.sleep(1)
    name = safe_input("What is your name:\n→ ").strip().title()
    time.sleep(1)
    confirm = safe_input(f"\nSo your name is {name}? (y/n): ").lower()

    if confirm == "y":
        state.player["name"] = name
        time.sleep(2)
        typewriter("\nInteresting...")
        time.sleep(1)
        typewriter("I wonder what path you'll take.")
        time.sleep(2)
        clear_screen()
        prompt_sound_setting()
        clear_screen()
        #bg_music_setting()
        clear_screen()
        Chapter_one_start()
    else:
        typewriter("Let's try again.\n")
        time.sleep(2)
        clear_screen()
        gameIntro()

# ───────────────────────────────────────────────
# DEV MODE
# ───────────────────────────────────────────────
# SOUND SETTING PROMPT
# ───────────────────────────────────────────────

def prompt_sound_setting():
    sound_input = safe_input("Would you like to keep the text sound enabled? (y/n): ").lower()
    if sound_input == "y":
        state.soundOP = True
        typewriter("Text sound has been enabled. You can disable it anytime by typing 'sound off'.")
    else:
        state.soundOP = False
        typewriter("Text sound has been turned off. You can enable it anytime by typing 'sound on'.")

def bg_music_setting():
    music_input = safe_input("Would you like to enable background music? (y/n): ").lower()
    if music_input == "y":
        state.musicOn = True
        typewriter("Background music has been enabled. You can disable it anytime by typing 'music off'.")
    else:
        state.musicOn = False
        typewriter("Background music has been turned off. You can enable it anytime by typing 'music on'.")
