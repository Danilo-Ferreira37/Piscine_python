class SecurePlant:
    """Represent a plant with valids informations"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Init the object Secure plant"""
        self.name = name
        self.__height = height
        self.__age = age
        self.__valid = True

    def set_height(self, height: int) -> None:
        """Check if height value is negative, if it is
            write the error and invalidate it """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__valid = False
        else:
            self.__height = height
            print(f"Height update: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Check if age value is negative, if it is
        write the error and invalidate it"""
        if age < 0:
            print(f"Invalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected")
            self.__valid = False
        else:
            self.__age = age
            print(f"Age updted: {self.__age} days [OK]")

    def show_info(self) -> None:
        """Show informations of the secure plant(object)"""
        print(f"Current plant: {self.name} "
              f"({self.__height}cm, {self.__age} days)")

    def verific_plant(self) -> int:
        """Return 1 if plant is valid and 0 if plant is not valid"""
        if self.__valid:
            return 1
        else:
            return 0


if __name__ == "__main__":
    """ """
    print("=== Garden Security System ===\n")
    plants = [SecurePlant("Rose", 0, 0),
              SecurePlant("Tulip", 0, 0),
              SecurePlant("Fern", 0, 0)]
    print(f"Plant created: {plants[0].name}")
    plants[0].set_height(5)
    plants[0].set_age(12)
    print("\n")
    plants[1].set_height(2)
    plants[1].set_age(-12)
    print("\n")
    plants[2].set_height(-7)
    plants[2].set_age(-80)
    print("\n")
    for plant in plants:
        if plant.verific_plant():
            plant.show_info()
