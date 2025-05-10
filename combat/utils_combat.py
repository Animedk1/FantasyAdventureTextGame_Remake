def get_health_bar(health, max_health, width=20):
    ratio = health / max_health
    filled = int(ratio * width)
    empty = width - filled

    try:
        # ANSI colors
        if ratio > 0.6:
            color = "\u001b[32m"  # Green
        elif ratio > 0.3:
            color = "\u001b[33m"  # Yellow
        else:
            color = "\u001b[31m"  # Red
        reset = "\u001b[0m"
        return f"{color}[{'█' * filled}{'░' * empty}]{reset} {int(ratio * 100)}%"
    except:
        # Fallback if ANSI not supported
        return f"[{'=' * filled}{' ' * empty}] {int(ratio * 100)}%"

def calculate_damage(attacker, defender, critical_chance=0.1):
    import random
    base_damage = attacker.strength * 2
    critical = random.random() < (critical_chance + attacker.intelligence * 0.01)
    if critical:
        base_damage *= 1.5
    return int(base_damage), critical
