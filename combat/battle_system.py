import time
import os
import state
from utils import typewriter, safe_input, clear_screen
from combat.utils_combat import get_health_bar, calculate_damage

def battle(player, enemy):
    typewriter(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        clear_screen()
        display_health(player, enemy)

        print("\nChoose your action:")
        print("a) Attack")
        print("b) Use Item")
        action = safe_input("→ ").lower()

        enemy_action = enemy.decide_action()

        # Player Turn
        if action == "a":
            damage, critical = calculate_damage(player, enemy)

            if enemy_action == "dodge":
                if attempt_dodge(enemy):
                    typewriter(f"The {enemy.name} dodged your attack!")
                else:
                    enemy.health -= damage
                    typewriter(f"You hit the {enemy.name} for {damage} damage.")
                    if critical:
                        typewriter("Critical Hit!")
            elif enemy_action == "defend":
                reduced = int(damage * 0.5)
                enemy.health -= reduced
                typewriter(f"The {enemy.name} defended. They took only {reduced} damage.")
            else:
                enemy.health -= damage
                typewriter(f"You hit the {enemy.name} for {damage} damage.")
                if critical:
                    typewriter("Critical Hit!")

        elif action == "b":
            use_item(player)  # Placeholder logic for now
        else:
            typewriter("Invalid action. You hesitate.")

        time.sleep(1)

        # Enemy Turn
        if enemy.is_alive():
            clear_screen()
            display_health(player, enemy)
            typewriter(f"The {enemy.name} is preparing to attack!")
            print("\nChoose your reaction:")
            print("a) Defend")
            print("b) Dodge")

            choice = timed_input("→ ", timeout=5).lower()

            defend = False
            dodge = False

            if choice == "a":
                defend = True
                typewriter("You brace for the incoming attack...")
            elif choice == "b":
                dodge = attempt_dodge(player)
                if dodge:
                    typewriter("You dodged the enemy’s attack!")
                    # Successful dodge deals chip damage back
                    chip = int(player.dexterity * 0.5)
                    enemy.health -= chip
                    typewriter(f"You counter slightly and deal {chip} damage to the {enemy.name}!")
                    continue
                else:
                    typewriter("You failed to dodge...")
            else:
                typewriter("You froze and did nothing!")

            damage, critical = calculate_damage(enemy, player)
            if defend:
                damage = int(damage * 0.5)
                if critical:
                    damage = int(damage * 1.5)
            player.health -= damage
            typewriter(f"The {enemy.name} hits you for {damage} damage.")
            if critical:
                typewriter("Critical Hit!")

        time.sleep(2)

    clear_screen()
    if player.is_alive():
        typewriter(f"\nYou defeated the {enemy.name}!")
    else:
        typewriter("\nYou were defeated...")

# Display both health bars at top of screen
def display_health(player, enemy):
    print(f"\n\u001b[1mYour Health:\u001b[0m  {get_health_bar(player.health, player.max_health)}")
    print(f"\u001b[1mEnemy Health:\u001b[0m {get_health_bar(enemy.health, enemy.max_health)}")

# Dodge logic
def attempt_dodge(combatant):
    import random
    return random.random() < (0.1 + combatant.dexterity * 0.02)

# Timed input fallback
def timed_input(prompt, timeout=5):
    import threading

    result = {"value": ""}

    def get_input():
        result["value"] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    return result["value"] if result["value"] else ""

# Placeholder item usage (expand later)
def use_item(player):
    typewriter("You fumble through your bag... but have no items yet.")
