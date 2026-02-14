class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunLightError(GardenError):
    pass


class GardenManager:
    def add_plant(self, plants: list):
        self.plants = []
        try:
            for plant in plants:
                if type(plant["name"]) != str and plant["name"] != None:
                    raise PlantNameError(f"Error adding plant: '{plant["name"]}' is invalid plant!")
                elif plant["name"] == None or plant["name"].strip() == "":
                    raise PlantNameError(f"Error adding plant: Plant name cannot be empty!")
                self.plants += [plant]
                print(f"added {plant["name"]} successfully")

        except PlantNameError as e:
            print(e)
    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant["water"] += 1 
                print(f"Watering {plant["name"]} - success")

        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self):
        try:
            for plant in self.plants:
                if plant["water"] > 10:
                    raise WaterLevelError(f"Error checking {plant["name"]}: Water level {plant["water"]} is too high (max 10)\n")
                elif plant["water"] < 1:
                    raise WaterLevelError(f"Error checking {plant["name"]}: Water level {plant["water"]} is too low (min 1)\n")
                elif plant["light"] < 2:
                    raise SunLightError(f"Error checking {plant["name"]}: Sunlight hours {plant["light"]} is too low (min 2)\n")
                elif plant["light"] > 12:
                    raise SunLightError(f"Error checking {plant["name"]}: Sunlight hours {plant["light"]} is too high (max 12)\n")
                print(f"{plant["name"]}: healtly (water: {plant["water"]}, sun: {plant["light"]})")
        except(WaterLevelError, SunLightError) as e:
            print(e)

def  test_garden_management():
    try:
        manager = GardenManager()

        print("Adding plants to garden...")
        manager.add_plant(plants = [{"name": "tomato", "water": 5 ,"light": 4 },
                                {"name":"lettuce","water": 3 ,"light": 1 },
                                {"name": None,"water": 22 ,"light": 9 }])

        print("\nWatering plants...")
        manager.water_plants()

        print("Checking plant health...")
        manager.check_plant_health()

        print("Testing error recovery...")
        raise GardenError("Caught GardenError: Not enough water in tank")
    except GardenError as e:
        print(e)
        print("System recovered and continuing...\n")
    finally:
        print("Garden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
