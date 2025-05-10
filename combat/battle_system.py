import time
import random
from combat.utils_combat import get_health_bar, calculate_damage, attempt_dodge, random_success
from utils import typewriter, safe_input, clear_screen
import state
from combat.combatants import Combatant

# ───────────────────────────────────────────────
# Main Battle Function
# Handles player-enemy interaction and battle loop
# ───────────────────────────────────────────────
def battle(player, enemy):
    typewriter(f"A wild {enemy.name} appears!")
    time.sleep(1)

    # Main battle loop
    while player.is_alive() and enemy.is_alive():
        clear_screen()
        print("============== BATTLE ==============")
        print("Your Health :", get_health_bar(player.health, player.max_health))
        print("Enemy Health:", get_health_bar(enemy.health, enemy.max_health))
        print("====================================\n")

        print("Choose your action:")
        print("a) Light Attack")   # High hit chance, lower damage
        print("b) Strong Attack")  # Lower hit chance, high damage
        print("c) Use Item")       # Placeholder for future item use

        action = safe_input("→ ").lower()
        enemy_action = enemy.decide_action()

        # Light attack logic
        if action == "a":
            damage, critical = calculate_damage(player, enemy, kind="light")
            if enemy_action == "dodge" and attempt_dodge(enemy):
                typewriter(f"The {enemy.name} dodged your light attack!")
            elif random_success(0.9):  # High success chance
                enemy.health -= damage
                typewriter(f"You hit the {enemy.name} for {damage} damage.")
                if critical:
                    typewriter("Critical Hit!")
            else:
                typewriter("Your attack missed!")

        # Strong attack logic
        elif action == "b":
            damage, critical = calculate_damage(player, enemy, kind="strong")
            if enemy_action == "dodge" and attempt_dodge(enemy):
                typewriter(f"The {enemy.name} dodged your strong attack!")
            elif random_success(0.6):  # Lower success chance
                enemy.health -= damage
                typewriter(f"You smash the {enemy.name} for {damage} damage.")
                if critical:
                    typewriter("Critical Hit!")
            else:
                typewriter("Your heavy swing misses its mark!")

        # Placeholder for item use
        elif action == "c":
            typewriter("You rummage through your items... (Item use not yet implemented.)")

        # Invalid input fallback
        else:
            typewriter("Invalid action. You hesitate.")

        time.sleep(1)

        # ───────────────────────────────────────────────
        # Enemy Turn + Player Defense Options (Dodge/Defend)
        # ───────────────────────────────────────────────
        if enemy.is_alive():
            print("\nThe enemy prepares to attack.")
            print("a) Dodge")
            print("b) Defend")

            reaction = safe_input("→ ").lower()
            dmg, critical = calculate_damage(enemy, player)

            if reaction == "a":
                if attempt_dodge(player):
                    typewriter("You successfully dodged!")
                    enemy.health -= 3  # Light counterattack
                    typewriter("You counter slightly while dodging! (3 damage)")
                else:
                    player.health -= dmg
                    typewriter(f"You failed to dodge. The {enemy.name} hits you for {dmg}.")
            elif reaction == "b":
                reduced = int(dmg * 0.5)
                if critical:
                    reduced = int(reduced * 1.5)
                player.health -= reduced
                typewriter(f"You defend. You take {reduced} damage.")
            else:
                player.health -= dmg
                typewriter(f"You hesitate. The {enemy.name} hits you for {dmg}.")

        time.sleep(2)

    # ───────────────────────────────────────────────
    # Battle outcome
    # ───────────────────────────────────────────────
    clear_screen()
    if player.is_alive():
        typewriter(f"\nYou defeated the {enemy.name}!")
    else:
        typewriter("\nYou were defeated...")

# ─────────────────────────────────────────────────────────────
# Helper used to trigger battle cleanly from main story chapters
# ─────────────────────────────────────────────────────────────
def start_battle(enemy, reward_gold=10, reward_item=None):
    player = Combatant(
        name=state.player["name"] or "Hero",
        health=state.player.get("health", 100),
        strength=state.player["stats"].get("strength", 5),
        intelligence=state.player["stats"].get("intelligence", 5),
        dexterity=state.player["stats"].get("dexterity", 5),
    )

    battle(player, enemy)

    # Update persistent player health after combat
    state.player["health"] = player.health

    # Victory rewards
    if player.is_alive():
        typewriter(f"You found {reward_gold} gold.")
        state.player["gold"] += reward_gold

        if reward_item:
            typewriter(f"You obtained: {reward_item}")
            state.player["inventory"].append(reward_item)
