from combat.enemies import create_shouting_man, create_peter_practice1
from combat.battle_system import start_battle




# ───────────────────────────────────────────────
# Battle Functions
# - A place to create wrapper funtions for battles
#   - Mainly to be able to create save points
# ───────────────────────────────────────────────

#Peter Tutorial Battle
def Peter_battle_tutorial():
    enemy = create_peter_practice1()
    start_battle(enemy, reward_gold=15, reward_item="Health Potion", intro_text= "Peter readys his Stance")