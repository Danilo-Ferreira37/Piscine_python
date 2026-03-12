from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
    
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
                'effect': self.effect
            }
        return {
            "insufficient mana": game_state.get("Mana")
        }
    
    def get_card_info(self):
        output_info = super().get_card_info()
        output_info['type'] = 'Creature'
        output_info['durability'] = self.durability
        output_info['effect'] = self.effect
        return output_info

    def activate_ability(self) -> dict:
        pass
