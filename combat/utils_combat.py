# combat/utils_combat.py

# ───────────────────────────────────────────────
# Utility: Health Bar Renderer
# ───────────────────────────────────────────────

def get_health_bar(health, max_health, width=20):
    """
    Creates a visual health bar using ANSI colors (if supported).
    Falls back to '=' style if ANSI isn't available.

    Args:
        health (int): Current health
        max_health (int): Maximum health
        width (int): Width of the bar in characters

    Returns:
        str: A formatted health bar string
    """
    ratio = max(0, health) / max_health
    filled = int(ratio * width)
    empty = width - filled

    try:
        if ratio > 0.6:
            color = "\u001b[32m"  # Green
        elif ratio > 0.3:
            color = "\u001b[33m"  # Yellow
        else:
            color = "\u001b[31m"  # Red
        reset = "\u001b[0m"
        return f"{color}[{'█' * filled}{'░' * empty}]{reset} {int(ratio * 100)}%"
    except:
        return f"[{'=' * filled}{' ' * empty}] {int(ratio * 100)}%"


# ───────────────────────────────────────────────
# Utility: Damage Calculator (Light or Strong)
# ───────────────────────────────────────────────

def calculate_damage(attacker, defender, kind="light"):
    """
    Calculates damage based on attacker strength and intelligence,
    including critical hit chance.

    Args:
        attacker (Combatant): Attacker object
        defender (Combatant): Defender object
        kind (str): 'light' or 'strong' determines range and crit risk

    Returns:
        Tuple (int damage, bool critical)
    """
    import random

    if kind == "light":
        base_damage = random.randint(6, 10)
        crit_multiplier = 1.5
        hit_multiplier = 1.0
    elif kind == "strong":
        base_damage = random.randint(12, 18)
        crit_multiplier = 2.0
        hit_multiplier = 1.0
    else:
        base_damage = random.randint(5, 10)

    crit_chance = 0.1 + (attacker.intelligence * 0.01)
    critical = random.random() < crit_chance

    final_damage = int(base_damage * crit_multiplier) if critical else int(base_damage * hit_multiplier)
    return final_damage, critical


# ───────────────────────────────────────────────
# Utility: Dodge Chance
# ───────────────────────────────────────────────

def attempt_dodge(combatant):
    """
    Returns True if dodge is successful, based on dexterity stat.

    Args:
        combatant (Combatant): The person attempting to dodge

    Returns:
        bool: Success or failure
    """
    import random
    return random.random() < (0.1 + combatant.dexterity * 0.02)


# ───────────────────────────────────────────────
# Utility: General Probability Check
# ───────────────────────────────────────────────

def random_success(chance):
    """
    Returns True or False based on the probability input (0.0 to 1.0)

    Args:
        chance (float): Success chance (e.g. 0.7 = 70%)

    Returns:
        bool
    """
    import random
    return random.random() < chance
