from ex0.CreatureCard import CreatureCard
from ex1 import SpellCard, Deck, ArtifactCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard(   ))
    deck.add_card(SpellCard(   ))
    deck.add_card(ArtifactCard(   ))
    print(f"Deck stats: {deck.get_deck_stats()}")


if __name__ == "__main__":
    main()
