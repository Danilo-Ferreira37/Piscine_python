import random
from ex0.Card import Card


class Deck():
    def __init__(self):
        self.cards = None
        self.total = 0

        self.creatures = 0
        self.spells = 0
        self.artifacts = 0

    def add_card(self, card: Card) -> None:
        if self.cards is None:
            self.cards = []
        self.cards.append(card)
        self.total += 1
        if card.card_type == "CreatureCard":
            self.creatures += 1

        elif card.card_type == "ArtifactCard":
            self.artifacts += 1

        elif card.card_type == "SpellCard":
            self.spells += 1

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                self.total -= 1 
                return True
        return False

    def shuffle(self) -> None:
        if self.cards:
            random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.total == 0:
            return None
        self.total -= 1
        card = self.cards.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        avg = 0
        try:
            for card in self.cards:
                avg += card.cost
            avg /= self.total
        except ZeroDivisionError:
            avg = 0
        except TypeError:
            pass
        return {'Deck status': {'total_cards': self.total, 'criatures': self.creatures,
                                'spells': self.spells, 'artifacts': self.artifacts,
                                'avg_cost': avg}}
