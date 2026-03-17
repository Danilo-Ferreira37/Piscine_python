from ex0.Card import Card, Rarity
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: Rarity,
                 effect_type: EffectType) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        val = 0
        if "mana" not in game_state and "Mana" not in game_state:
            return {"error": "The key has to be mana!"}
        mana_key = "mana" if "mana" in game_state else "Mana"
        val = game_state[mana_key]

        if self.is_playable(val):
            game_state[mana_key] -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect_type
            }
        return {
            "insufficient mana": game_state.get("Mana")
        }

    def get_card_info(self) -> dict:
        output_info = super().get_card_info()
        output_info['type'] = 'Creature'
        output_info['effect_type'] = self.effect_type
        return output_info

    def resolve_effect(self, targets: list) -> dict:
        return {targets: self.effect_type}
