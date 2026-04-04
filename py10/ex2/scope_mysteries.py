from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def power_accum(add_power) -> int:
        nonlocal total
        total += add_power
        return total
    return power_accum


def enchantment_factory(enchantment_type: str) -> callable:

    def enchant_item(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant_item


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> dict:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")
    flame_item = enchantment_factory("Flaming")
    freeze_item = enchantment_factory("Freeze")
    print(flame_item("Sword"))
    print(freeze_item("Shield"))


if __name__ == "__main__":
    main()
