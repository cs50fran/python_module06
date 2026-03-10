import alchemy.elements
import alchemy.potions
from alchemy.potions import strength_potion, healing_potion as heal
from alchemy.elements import create_fire, create_water, create_earth


def main() -> None:
    print("=== Import Transmutation Mastery ===")

    fire = create_fire()
    water = create_water()
    earth = create_earth()

    print("\nMethod 1 - Full module import:")
    print(f"alchemy.element.create_fire(): {alchemy.elements.create_fire()}")

    print("\nMethod 2 - Specific function import:")
    print(f"create.water(): {water}")

    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal(water, fire)}")

    print("\nMethod 4 - Multiple imports:")
    print(f"create.earth(): {earth}")
    print(f"create.fire(): {create_fire()}")
    print(f"strengh_potion(): {strength_potion(earth, fire)}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
