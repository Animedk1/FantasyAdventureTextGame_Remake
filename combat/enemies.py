from combat.combatants import Combatant
import random

class Enemy(Combatant):
    def __init__(self, name, health, strength, intelligence, dexterity, behavior="balanced"):
        super().__init__(name, health, strength, intelligence, dexterity)
        self.behavior = behavior

    def decide_action(self):
        if self.behavior == "aggressive":
            return random.choices(["attack", "defend", "dodge"], weights=[0.6, 0.2, 0.2])[0]
        elif self.behavior == "defensive":
            return random.choices(["attack", "defend", "dodge"], weights=[0.3, 0.5, 0.2])[0]
        else:
            return random.choices(["attack", "defend", "dodge"], weights=[0.4, 0.3, 0.3])[0]

# First enemy: Shouting Man from Tavern
def create_shouting_man():
    return Enemy(name="Shouting Man", health=100, strength=6, intelligence=4, dexterity=3, behavior="aggressive")
