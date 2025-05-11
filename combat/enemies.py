# combat/enemies.py

from combat.combatants import Combatant
import random

# ───────────────────────────────────────────────
# Enemy class extends Combatant with AI behavior
# ───────────────────────────────────────────────

class Enemy(Combatant):
    def __init__(self, name, health, strength, intelligence, dexterity, behavior="balanced"):
        """
        Represents an enemy in battle with its own behavior.

        Args:
            name (str): Enemy name
            health (int): Max and starting health
            strength (int): Damage potential
            intelligence (int): Crit chance modifier
            dexterity (int): Dodge capability
            behavior (str): AI style - 'aggressive', 'defensive', 'balanced'
        """
        super().__init__(name, health, strength, intelligence, dexterity)
        self.behavior = behavior

    def decide_action(self):
        """
        AI chooses a behavior each turn based on its assigned strategy.
        Returns: 'attack', 'defend', or 'dodge'
        """
        if self.behavior == "aggressive":
            return random.choices(["attack", "defend", "dodge"], weights=[0.6, 0.2, 0.2])[0]
        elif self.behavior == "defensive":
            return random.choices(["attack", "defend", "dodge"], weights=[0.3, 0.5, 0.2])[0]
        else:  # balanced
            return random.choices(["attack", "defend", "dodge"], weights=[0.4, 0.3, 0.3])[0]

# ───────────────────────────────────────────────
# Predefined Enemy Types
# Extend this section with more enemies over time
# ───────────────────────────────────────────────

def create_shouting_man():
    """
    First encounter enemy introduced during the tavern scene.
    Aggressive but not overpowered.
    """
    return Enemy(
        name="Shouting Man",
        health=100,
        strength=6,
        intelligence=4,
        dexterity=3,
        behavior="aggressive"
    )

def create_peter_practice1():
    """
    Practice Encounter with NPC Peter.
    Balanced

    """
    return Enemy(
        name="Peter_Chpt1_Practice",
        health=100,
        strength=2,
        intelligence=4,
        dexterity=3,
        behavior="aggressive"
    )
