import sys

if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        inventory = {}
        total = 0
        unique_item = 0
        if len(sys.argv) < 2:
            raise Exception("Error: No argument was made!! "
                            "You need to enter a dictionary!")
        for arg in sys.argv[1:]:
            if ":" in arg:
                item, qnty = arg.split(":")
                inventory.update({item: int(qnty)})
                unique_item += 1
            else:
                raise Exception("Error You need to enter a dictionary")

        for qnty in inventory.values():
            total += qnty
            if qnty < 0:
                raise ValueError
        print(f"Total item in inventory {total}")
        print(f"Unique item types: {unique_item}")

        print("\n=== Current Inventory ===")
        for item in inventory:
            if inventory[item] == 0:
                print(f"{item}: {inventory[item]} unit (0%)")
            elif inventory[item] > 1:
                print(f"{item}: {inventory[item]} units "
                      f"({inventory[item] /  total * 100:.1f}%)")
            else:
                print(f"{item}: {inventory[item]} unit "
                      f"({inventory[item] /  total * 100:.1f}%)")

        print("\n === Inventory Statistics ===")

        max = None
        item_max = None
        for item, qnty in inventory.items():
            if max is None or qnty > max:
                max = qnty
                item_max = item
        if max > 1:
            print(f"Most abundant: {item_max} ({max} units)")
        else:
            print(f"Most abundant: {item_max} ({max} unit)")

        min = None
        item_min = None
        for item, qnty in inventory.items():
            if min is None or qnty < min:
                min = qnty
                item_min = item
        if min > 1:
            print(f"Most abundant: {item_min} ({min} units)")
        else:
            print(f"Most abundant: {item_min} ({min} unit)")

        print("\n=== Item Categories ===")
        moderate = {}
        scarce = {}
        very_scarce = []
        for item, qnty in inventory.items():
            if qnty >= 4:
                moderate.update({item: qnty})
            else:
                scarce.update({item: qnty})
                if qnty == 1:
                    very_scarce += [item]

        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {very_scarce}")

        print("\n=== Dictionary Properties Demo ===")
        itens = []
        values = []
        lookup = "sword"
        condition = False
        for item, qnty in inventory.items():
            itens += [item]
            values += [qnty]
            if item == lookup:
                condition = True
        print(f"Dictionary keys: {itens}")
        print(f"Dictionary values: {values}")
        print(f"Sample lookup - {lookup} in inventory: {condition}")
    except ValueError:
        print("Error: The value has to be a positive integer")
    except Exception as e:
        print(e)
