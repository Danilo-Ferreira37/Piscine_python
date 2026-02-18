def  check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str | None:
    try:
        if plant_name == None or plant_name.strip() == "":
            raise ValueError("Error: Plant name cannot be empty!\n")
        elif water_level > 10:
            raise ValueError(f"Error: Water level {water_level} is too high (max 10)\n")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} is too low (min 1)\n")
        elif sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)\n")
        return f"Plant '{plant_name}' is healthy!\n"
    except ValueError as e:
        print(e)

def test_plant_checks() -> None:
    print("Testing good values...")
    print(check_plant_health("tomato", 6, 11))

    print("Testing empty plant name...")
    check_plant_health("", 6, 11)

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 11)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 6, 0)

if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
