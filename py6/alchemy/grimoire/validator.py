def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    for elem in valid_elements:
        if elem in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
