# combat/combatants.py

# ───────────────────────────────────────────────
# Base class for all combatants (Player or Enemy)
# Handles stats and health behavior
# ───────────────────────────────────────────────

class Combatant:
    def __init__(self, name, health, strength, intelligence, dexterity):
        """
        Represents a character in battle (player or enemy).
        
        Args:
            name (str): Combatant's name
            health (int): Current and max health
            strength (int): Affects physical damage
            intelligence (int): Affects crit chance
            dexterity (int): Affects dodge success
        """
        self.name = name
        self.max_health = health
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity

    def is_alive(self):
        """
        Check if the combatant is still alive.
        """
        return self.health > 0
