from ex0.Card import Card

class Deck():
    def add_card(self, card: Card) -> None:
        if self.cards is None:
            self.cards = []
        self.cards.append(card)
        self.total += 1
        self.criatures = 0
        self.spells = 0
        self.artifacts = 0

    def remove_card(self, card_name: str) -> bool:
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        return {'Deck status': {'rotal_cards': self.total, 'criatures': self.criatures, 'spells': self.spells, 'artifacts': self.artifacts}}