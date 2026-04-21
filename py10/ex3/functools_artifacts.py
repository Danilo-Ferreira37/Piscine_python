from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not all(isinstance(n, int) for n in spells):
        raise ValueError("Error: The spells has be integer")
    if operation not in ("max", "sum", "min", "product"):
        raise ValueError("Error: The operation has be max, min, sum, product")

    if operation == "sum":
        return reduce(operator.add, spells)
    if operation == "product":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(lambda a, b: a if operator.gt(a, b) else b, spells)
    if operation == "min":
        return reduce(lambda a, b: a if operator.lt(a, b) else b, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, 50, "Fire")
    ice = partial(base_enchantment, 50, "Ice")
    lightning = partial(base_enchantment, 50, "Lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Error: The fibonacci number has to be a integer")
    if n == 1 or n == 0:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatcher(spell) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @dispatcher.register(int)
    def _(spell) -> str:
        return f"Damage spell cast for {spell} points!"

    @dispatcher.register(str)
    def _(spell) -> str:
        return f"Enchantment applied: {spell}"

    @dispatcher.register(list)
    def _(spell) -> str:
        return [dispatcher(s) for s in spell]

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{power} {element} {target}"


def main() -> None:
    try:
        print("\nTesting spell reducer...")
        spells = [10, 20, 30, 40]
        print(f"Sum: {spell_reducer(spells, "sum")}")
        print(f"Product: {spell_reducer(spells, "product")}")
        print(f"Max: {spell_reducer(spells, "min")}")

        print("\nTesting memoized fibonacci...")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(f"Error: The keyword has to be {e}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
