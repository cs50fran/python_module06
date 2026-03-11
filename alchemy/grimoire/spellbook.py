def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import breaks the circular dependency:
    # __init__.py imports spellbook, so a top-level
    # 'from alchemy.grimoire import validate_ingredients'
    # here would loop back into __init__.py before it finishes loading.
    # Importing inside the function defers resolution until call time.
    from alchemy.grimoire.validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if "- VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
