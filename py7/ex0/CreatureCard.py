from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity:
                 Rarity, attack: int, health: int):
        try:
            super().__init__(name, cost, rarity)
            if attack < 0:
                raise ValueError("Attack must be a positive integer.")
            self.attack = attack

            if health < 0:
                raise ValueError("Health must be a positive integer.")
            self.health = health
        except ValueError as e:
            print(e)

    def __str__(self):
        return f"{self.name} ({self.cost})"

    def get_card_info(self):
        output_info = super().get_card_info()
        output_info['type'] = 'Creature'
        output_info['attack'] = self.attack
        output_info['health'] = self.health
        return output_info

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
                'effect': "Creature summoned to battlefield"
            }
        return {
            "insufficient mana": game_state.get("Mana")
        }

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
