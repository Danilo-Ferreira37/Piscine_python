from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args: Any, **kwargs: Any) -> str:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args: Any, **kwargs: Any) -> str:
        return base_spell(*args, **kwargs) * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def condicional(*args: Any, **kwargs: Any) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return condicional


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args: Any, **kwargs: Any) -> callable:
        return [s(*args, **kwargs) for s in spells]
    return sequence


def fireball_spell(target: str) -> str:
    return f"Fireball hits {target}"


def heal_spell(target: str) -> str:
    return f"Heals {target}"


def lightning_spell(target: str) -> str:
    return f"Lightning hits {target}"


def dragon_power() -> int:
    return 10


def is_target_alive(target: str) -> str:
    return target != "dead"


def main() -> None:
    try:
        print("\nTesting spell combiner...")
        combined = spell_combiner(fireball_spell, heal_spell)
        output = combined("Dragon")
        print(f"Combined spell result: {output[0]}, {output[1]}")

        print("\nTesting power amplifier...")
        amplifier = power_amplifier(dragon_power, 3)
        print(f"Original: {dragon_power()}, Amplifield: {amplifier()}")
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(f"Error: The keyword has to be {e}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
