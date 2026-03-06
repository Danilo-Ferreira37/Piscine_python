from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    creature = CreatureCard('Fire Dragon', 5, 'Legendary', 7,  5)
    print(creature.get_card_info())

    mana = 6
    print(f"\nPlaying {creature.name} with {mana} mana available:")
    print(f"Playable {creature.is_playable(mana)}")
    print(f"Play result: {creature.play({'Mana': mana})}")

    enemie = "Goblin Warrior"
    print(f"\nFire Dragon attacks {enemie}:")
    print(f"Attack result: {creature.attack_target(enemie)}")

    insu_mana = 3
    print(f"\nTesting insuficient mana ({insu_mana} available)")
    print(f"Playable: {creature.is_playable(insu_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
