class Plant:
    def __init__(self, name: str, height: int, age: int, score: int):
        """Basic plant with name, height, age and score."""
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        self.score = score


class FloweringPlant(Plant):
    def __init__(self, name, height, age, score, color: str):
        """Plant that produces flowers with a specific color."""
        super().__init__(name, height, age, score)
        self.color = color

    def bloom(self) -> str:
        """Return blooming message."""
        return f"{self.name} bloom perfectly"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, rarity: str):
        """Special flower with rarity-based score."""
        super().__init__(name, height, age, 0, color="golden")
        self.rarity = rarity
        if rarity == "Legendary":
            self.score = 80
        elif rarity == "Mytic":
            self.score = 40
        elif rarity == "Rare":
            self.score = 20

    def glow_intensive(self) -> str:
        """Return glowing message."""
        return f"{self.name} glow golden like the gold"


class Garden:
    def __init__(self, name: str, plants: list = None):
        """Garden containing multiple plants."""
        self.name = name
        self.growth = 0
        if plants:
            self.plants = plants
        else:
            self.plants = []
        self.quantity = 0
        for _ in self.plants:
            self.quantity += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.quantity += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_plants(self) -> None:
        """Grow all plants in the garden."""
        print(f"{self.name} is helping all plants grow ...")
        for plant in self.plants:
            self.growth += 2
            plant.height += 2
            print(f"{plant.name} grew 2cm")


class GardenManager:
    def __init__(self, gardens: list):
        """Manage multiple gardens."""
        self.gardens = gardens
        self.quantity = 0
        for _ in self.gardens:
            self.quantity += 1

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Create a predefined garden network."""
        my_garden = Garden("Danilo")
        your_garden = Garden("Alice")
        our_garden = Garden("Ingrig")
        manager = cls([my_garden, your_garden, our_garden])

        my_garden.add_plant(PrizeFlower("Sunflower", 100, 80, "Legendary"))
        my_garden.add_plant(PrizeFlower("Babosa", 25, 365 * 2, "Mytic"))
        your_garden.add_plant(FloweringPlant("Rose", 15, 30, 0, "red"))
        our_garden.add_plant(Plant("Plantinha", 50, 20, 0))

        print("")
        my_garden.grow_plants()
        print("")
        stats = manager.GardenStats(manager)

        stats.report_garden(my_garden)
        stats.height_validation(my_garden)
        print(stats.count_score())
        stats.count_garden()

        return manager

    class GardenStats:
        def __init__(self, manager: "GardenManager"):
            """Statistics and reports for gardens."""
            self.n_gardens = 0
            self.manager = manager

        def count_garden(self) -> None:
            """Print total number of gardens."""
            for _ in self.manager.gardens:
                self.n_gardens += 1
            print(f"Total gardens managed: {self.n_gardens}")

        def count_score(self) -> str:
            """Return total score of each garden."""
            result = "Garden scores - "
            first = True
            for garden in self.manager.gardens:
                score = 0
                for plant in garden.plants:
                    score += plant.score
                if first:
                    result += f"{garden.name}: {score}"
                    first = False
                else:
                    result += f", {garden.name}: {score}"

            return result

        @staticmethod
        def report_garden(garden: Garden) -> None:
            """Print detailed report of a garden."""
            print(f"=== {garden.name}'s Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                if "rarity" in plant.__dict__:
                    print(f"- {plant.name}: {plant.height}cm "
                          f"{plant.color} flowers (blooming), "
                          f"Prize points: {plant.score}")
                elif "color" in plant.__dict__:
                    print(f"- {plant.name}: {plant.height}"
                          f"cm {plant.color} flowers, (blooming)")
                else:
                    print(f"- {plant.name}: {plant.height}cm")
            print()
            print(f"Plants added: {garden.quantity},"
                  f" Total growth: {garden.growth}cm")
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if "color" in plant.__dict__:
                    flowering += 1
                elif "rarity" in plant.__dict__:
                    prize += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers\n")

        @staticmethod
        def height_validation(garden: Garden) -> None:
            """Validate if all plant heights are non-negative."""
            valid = True
            for plant in garden.plants:
                if plant.height < 0:
                    valid = False
            print(f"Height validation test: {valid}")


if __name__ == "__main__":
    print("=== Garden Managment System Demo ===\n")
    manager = GardenManager.create_garden_network()
