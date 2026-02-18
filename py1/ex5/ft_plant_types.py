class Plant:
    """Represents a plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Inicialize the plants"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a plant. """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize the plant."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print bloom message. """
        print(f"{self.name} is blooming beautifully!\n")

    def show_info_flower(self) -> None:
        """Show flower information. """
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    """Represents a tree. """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Print shade information. """
        print(f"{self.name} provides 58 square meters of shade\n")

    def show_info_tree(self) -> None:
        """Show tree information. """
        print(f"{self.name} (Tree): {self.height}cm, {self.age} "
              f"days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Represents a vegetable. """
    def __init__(
            self, name: str, height: int, age: int,
            harvest_season: str, nutricional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value

    def nutricional_values(self) -> None:
        """Print nutritional value. """
        print(f"{self.name} is {self.nutricional_value}\n")

    def show_info_vegetable(self) -> None:
        """Show vegetable information. """
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 10, 40, "pink")
    rose.show_info_flower()
    rose.bloom()

    sunflower = Flower("Sunflower", 20, 30, "yellow")
    sunflower.show_info_flower()
    sunflower.bloom()

    oak = Tree("Oak", 3 * 60, 365 * 2, 6)
    oak.show_info_tree()
    oak.produce_shade()

    spruce = Tree("Spruce", 10 * 60, 365 * 21, 20)
    spruce.show_info_tree()
    spruce.produce_shade()

    carrot = Vegetable("Carrot", 20, 30, "spring", "rich in vitamin C")
    carrot.show_info_vegetable()
    carrot.nutricional_values()

    lettuce = Vegetable("Lettuce", 15, 40, "winter", "rich in vitamin B12")
    lettuce.show_info_vegetable()
    lettuce.nutricional_values()
