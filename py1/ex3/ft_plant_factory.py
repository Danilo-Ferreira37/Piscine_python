class Plant:
    """Represents a plant."""
    def __init__(self, name: str, height: int, age: int):
        "init tha plant"
        self.name = name
        self.height = height
        self.age = age

    def show_info(self) -> None:
        """Show plant information"""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    """Create plants"""
    plants = [Plant("Rose", 10, 30),
              Plant("Tulip", 15, 10),
              Plant("Sunflower", 85, 200),
              Plant("Cactus", 200, 100),
              Plant("Fern", 15, 120)]
    quantity = 0

    print("=== Plant Factory Output ===")
    for i in plants:
        i.show_info()
        quantity += 1

    print(f"\nTotal plants created: {quantity}")
