from ex0.Card import Card, EffectType

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: EffectType):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass

