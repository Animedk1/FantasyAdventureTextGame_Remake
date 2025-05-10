class Combatant:
    def __init__(self, name, health, strength, intelligence, dexterity):
        self.name = name
        self.max_health = health
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity

    def is_alive(self):
        return self.health > 0
