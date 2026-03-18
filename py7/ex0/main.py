from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")

        print("CreatureCard Info:")
        creature = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 7,  5)
        print(creature.get_card_info())

        mana = 6
        print(f"\nPlaying {creature.name} with {mana} mana available:")
        print(f"Playable {creature.is_playable(mana)}")
        print(f"Play result: {creature.play({'Mana': mana})}")

        enemie = "Goblin Warrior"
        print(f"\nFire Dragon attacks {enemie}:")
        print(f'Attack result: {creature.attack_target(enemie)}')

        insu_mana = 3
        print(f"\nTesting insuficient mana ({insu_mana} available)")
        print(f"Playable: {creature.is_playable(insu_mana)}")

        print("\nAbstract pattern successfully demonstrated!")

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
