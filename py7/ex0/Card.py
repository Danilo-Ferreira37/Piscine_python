from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    UNCOMMON = "Uncommon"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        self.name = name
        if not isinstance(cost, int):
            raise ValueError("Error: The cost of card has to be a integer")
        if not rarity in Rarity.__members__.values():
            raise ValueError("Error: Rarity is invalid,"
                  " the rarity has to be Common, Rare, Epic, Legendary")
        self.cost = cost
        self.rarity = rarity.value
        self.card_type = self.__class__.__name__

    def __str__(self) -> str:
        return f"{self.name} ({self.cost})"

    def __repr__(self) -> str:
        return self.__str__()

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
