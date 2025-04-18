import os
import json
import time
from utils import typewriter, clear_screen, safe_input
from state import player, game_state
from chapters.chapter_one import Chapter_one_start

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
        save_data = {"player": player, "game_state": game_state}
        with open(get_save_path(), "w") as f:
            json.dump(save_data, f)
        typewriter("\nGame saved successfully!\n")
    except Exception as e:
        typewriter(f"\nFailed to save game: {e}")

def load_game():
    global player, game_state
    try:
        with open(get_save_path(), "r") as f:
            save_data = json.load(f)
            # Update in place instead of replacing
            player.clear()
            player.update(save_data.get("player", {}))

            game_state.clear()
            game_state.update(save_data.get("game_state", {}))

        typewriter("\nGame loaded successfully!\n")
        time.sleep(1)
        clear_screen()
        resume_checkpoint(player.get("checkpoint", "intro"))
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
    if point == "intro":
        gameIntro()
    elif point == "chapter_one":
        Chapter_one_start()
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
    player["checkpoint"] = "intro"
    typewriter("Your Journey begins here, but before you venture forth...")
    time.sleep(1)
    name = safe_input("What is your name:\n→ ").strip().title()
    time.sleep(1)
    confirm = safe_input(f"\nSo your name is {name}? (y/n): ").lower()

    if confirm == "y":
        player["name"] = name
        time.sleep(2)
        typewriter("\nInteresting...")
        time.sleep(1)
        typewriter("I wonder what path you'll take.")
        time.sleep(2)
        clear_screen()
        Chapter_one_start()
    else:
        typewriter("Let's try again.\n")
        time.sleep(2)
        clear_screen()
        gameIntro()
