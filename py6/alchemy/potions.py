from .elements import create_air, create_earth, create_fire, create_water


def healing_potion():
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strenght_potion():
    fire = create_fire()
    earth = create_earth()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion():
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion():
    fire = create_fire()
    air = create_air()
    earth = create_earth()
    water = create_water()
    return (f"Wisdom potion brewed with all elements: {fire}, {air}, {earth},"
            f"{water}")
