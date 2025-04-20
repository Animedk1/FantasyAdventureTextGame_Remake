# ───────────────────────────────────────────────
# PLAYER STATE
# ───────────────────────────────────────────────
player = {
    "name": "",
    "gold": 0,
    "inventory": [],
    "armored": False,
    "checkpoint": "intro",  # Default starting location
    "stats": {
        "strength": 5,
        "dexterity": 5,
        "intelligence": 5,
    },
    "relationships": {
        "Erena": 0,
        "Markus": 0,
    }
}

# ───────────────────────────────────────────────
# WORLD STATE
# ───────────────────────────────────────────────
game_state = {
    "met_mysterious_voice": False,
    "has_cursed_item": False,
    "sided_with_faction": None,
    "chapter_events": {},
    "shop_unlocked": False,
    
    # Flags for characters the player has met
    "erena_met": False,
    "markus_met": False
}

# ───────────────────────────────────────────────
# Sound STATE
# ───────────────────────────────────────────────
# state.py

soundOP = True  # Default: sound is ON

