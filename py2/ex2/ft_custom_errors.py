class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant(plant_condition: str) -> None:
    print("Testing PlantError...")
    try:
        if plant_condition == "wilted" or plant_condition == "Wilted":
            raise PlantError("The tomato plant is wilted!")
        print("Plants it's fine\n")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

def test_irrigation(tank: int) -> None:
    print("Testing WaterError...")
    try:
        if tank <= 2:
            raise WaterError("Not enough water in the tank!")
        print("Water system OK\n")
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

def all_erros(condition: str, tank: int) -> None:
    print("Testing catching all garden errors...")
    try:
        if condition == "wilted" or condition == "Wilted":
            raise PlantError("The tomato plant is wilted!")
        print("Plants it's fine")
    except GardenError as e:
        print(f"Caught garden error: {e}!")
    
    try:
        if tank <= 2:
            raise WaterError("Not enough water in the tank!")
        print("Water system OK")
    except GardenError as e:
        print(f"Caught garden error: {e}!")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant("Wilted")
    test_irrigation(2)
    all_erros("wilted", -98989)

    print("\nAll custom error types work correctly!")
