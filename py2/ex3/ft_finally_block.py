def water_plants(plant_list: list) -> None:
    print("Opening waterning system")
    success = True
    try:
        for plant in plant_list:
            if type(plant) != str:
                success = False
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Waterning {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        if success == True:
            print("Closing waterning system (cleanup)")
            print("Watering completed successfully!\n")
        else:
            print("Closing waterning system (cleanup)\n")

def test_waterning_system() -> None:
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal waterning...")
    water_plants(plants)

    error = ["tomato", None]
    print("Testing with error...")
    water_plants(error)

if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_waterning_system()
    print("Cleanup always happens, even with errors!")
