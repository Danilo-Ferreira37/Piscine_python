class Plant:
    """Represents a plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def get_info(self) -> str:
        """Get plant information"""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self) -> None:
        """Grow the plant"""
        self.height += 2
        self.growth += 2

    def age_plant(self) -> None:
        """Increases age of the plant"""
        self.age += 1


if __name__ == "__main__":
    """Performs plant information."""
    plants = [Plant("Rose", 25, 30),
              Plant("Tulip", 15, 10),
              Plant("Sunflower", 40, 50)]
    print("=== Day 1 ===")
    for i in plants:
        print(i.get_info())

    for i in plants:
        for _ in range(6):
            i.grow()
            i.age_plant()

    print("\n=== Day 7 ===")
    for i in plants:
        print(i.get_info())

    print("\nGrowth this week:")
    for i in plants:
        print(f"{i.name}: {i.growth}cm")
