import time
import sys
import os
from state import player, game_state

# ───────────────────────────────────────────────
# SYSTEM UTILITIES
# ───────────────────────────────────────────────

def typewriter(text, delay=0.05):
    for char in text:
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

# ───────────────────────────────────────────────
# DEFAULT DISPLAY FUNCTIONS
# ───────────────────────────────────────────────

def show_stats():
    # Show basic stats
    typewriter(f"\nName: {player['name'] or 'Unknown'}")
    typewriter(f"Gold: {player['gold']}")
    typewriter(f"Armored: {'Yes' if player['armored'] else 'No'}")

    # Player attributes
    typewriter("\nStats:")
    for stat, value in player["stats"].items():
        typewriter(f"  {stat.title()}: {value}")

    # Only show Relationships section if at least one person is met
    met_anyone = game_state.get("erena_met") or game_state.get("markus_met")
    if met_anyone:
        typewriter("\nRelationships:")
        if game_state.get("erena_met"):
            typewriter(f"  Erena: {player['relationships'].get('Erena', 0)}")
        if game_state.get("markus_met"):
            typewriter(f"  Markus: {player['relationships'].get('Markus', 0)}")
def show_inventory():
    if player["inventory"]:
        typewriter("\nYou're carrying:")
        for item in player["inventory"]:
            typewriter(f"- {item}")
    else:
        typewriter("\nYour inventory is empty.")

# ───────────────────────────────────────────────
# INPUT HANDLER (with commands)
# ───────────────────────────────────────────────

def get_choice(valid_choices):
    from backend import save_game, load_game, delete_save
    while True:
        choice = safe_input().lower()

        if choice == "help":
            print("\u001b[33mAvailable Commands:\u001b[0m")
            print("  \u001b[1mstats\u001b[0m     - View your character stats and relationships")
            print("  \u001b[1minventory\u001b[0m - See what items you're carrying")
            print("  \u001b[1mgold\u001b[0m      - Check how much gold you have")
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
            print(f"\nYou currently have {player['gold']} gold.\n")
        elif choice == "save":
            save_game()
        elif choice == "load":
            load_game()
        elif choice in ["restart", "delete"]:
            delete_save()
        elif choice in valid_choices:
            return choice
        else:
            typewriter("Invalid choice. Try again.")
