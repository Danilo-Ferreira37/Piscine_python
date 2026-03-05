def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as val
    return (f"Spell recorded: {spell_name} ({val(ingredients)})"
            if val(ingredients) == f"{ingredients} - VALID"
            else f"Spell rejected: {spell_name} ({val(ingredients)})")
