from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.n_cards = 0
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")

    def simulate_turn(self) -> dict:
        hand = self.factory.create_themed_deck(3)
        print("Available types:", self.factory.get_supported_types())
        print("\nSimulating aggressive turn...")
        hand_filtered = hand["creatures"]
        hand_filtered += hand["spells"]
        hand_filtered += hand["artifacts"]
        hs = []
        for card in hand_filtered:
            self.n_cards += 1
            hs += [f'{card["name"]} ({card["cost"]})']
        print(f"Hand: {hs}\n")

        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {self.strategy.execute_turn(hand_filtered, [])}")

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.strategy.total_turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.strategy.total_damage,
            'cards_created': self.n_cards
        }

