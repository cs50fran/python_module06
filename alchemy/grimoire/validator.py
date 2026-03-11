VALID_ELEMENTS = {"fire", "water", "earth", "air"}


def validate_ingredients(ingredients: str) -> str:
    for element in VALID_ELEMENTS:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
