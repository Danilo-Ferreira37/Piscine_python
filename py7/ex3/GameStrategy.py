from ex0.Card import Card 
from ex1.SpellCard import SpellCard
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
