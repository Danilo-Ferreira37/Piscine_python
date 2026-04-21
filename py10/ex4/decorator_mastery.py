from functools import wraps
from typing import Any
import time


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)

        end = time.time()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    if not isinstance(min_power, int):
        raise ValueError("Error: The minimun power has to be a integer!")

    def decorator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | str:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[2]
            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    current_attempt = 1

    def decorator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception:
                nonlocal current_attempt
                if current_attempt > max_attempts:
                    return (f"Spell casting failed after "
                            f"{max_attempts} attempts")
                print(f"Spell failed, retrying... ("
                      f"{current_attempt} n/{max_attempts})")
                current_attempt += 1
                return wrapper(*args, **kwargs)
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    enemy = "alive"
    for _ in range(100_000):
        enemy = "dead"
    callable(enemy)
    return "Fireball cast!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        if not all(c.isalpha() or c.isspace() for c in name):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    try:
        print("\nTesting spell timer...")
        print(f"Result: {fireball()}")

        print("\nTesting MageGuild...")
        m_guild = MageGuild()
        print(m_guild.validate_mage_name("Danilo Ferreira"))
        print(m_guild.validate_mage_name("Robot 3737"))
        print(m_guild.cast_spell("Lightning", 15))
        print(m_guild.cast_spell("Blood Curse", 4))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
