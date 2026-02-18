class Plant:
    """Represents a plant."""
    def __init__(self, name: str, height: int, age: int):
        """Init the plant"""
        self.name = name
        self.height = height
        self.age = age

    def show_info(self) -> None:
        """Display plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    """Performs plant information."""
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.show_info()
    plant2.show_info()
    plant3.show_info()
