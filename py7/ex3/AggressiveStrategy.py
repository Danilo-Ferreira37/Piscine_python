from ex3.GameStrategy import GameStrategy
import random

class AgressiveStrategy(GameStrategy):
    def __init__(self):
        self.cards_played = []
        self.total_turns = 0
        self.mana_used = 0
        self.total_damage = 0

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        self.total_turns += 1

        for card in hand[:]:
            if card["cost"] < 4:
                self.cards_played.append(card["name"])
                self.mana_used += card["cost"]
                battlefield.append(card)
                hand.remove(card)
        for creature in battlefield:
            self.total_damage += creature.get("attack", 0)
        return {
                'cards_played': self.cards_played,
                'mana_used': self.mana_used,
                'targets_attacked': ['Enemy Player'],
                'damage_dealt': self.total_damage
        }
            
    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list) -> list:
        random.shuffle(available_targets)
        return available_targets
