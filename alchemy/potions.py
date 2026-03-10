def healing_potion() -> str:
    from .elements import create_fire, create_water
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    fire = create_fire()
    earth = create_earth()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    from .elements import create_earth, create_air, create_fire, create_water
    all_elements = (f"{create_fire()}, "
                    f"{create_water()}, "
                    f"{create_earth()}, "
                    f"{create_air()}")
    return f"Wisdom potion brewed with all elements: {all_elements}"
