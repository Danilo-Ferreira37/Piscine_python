from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard('Lightning Bolt', 3, 'Epic', 'Deal 3 damage to target'))
    deck.add_card(ArtifactCard('Mana Crystal', 2, "Common", 10, 'Permanent: +1 mana per turn'))
    deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5))
    deck.add_card(CreatureCard('Danilo GOAT', 3, 'Legendary', 45, 11111))
    deck.remove_card('Danilo GOAT')

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")
    deck.shuffle()

    game_state = {"mana": 10}
    for card in deck.cards[:3]:
        print(f"Drew: {card.name} ({card.card_type.replace('Card', '')})")
        print(f"Play result: {card.play(game_state)}\n")
        deck.draw_card()

    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()
