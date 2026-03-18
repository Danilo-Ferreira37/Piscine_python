from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: Rarity, damage: int,
                 health: int, defense: int, id: str) -> str:
        super().__init__(name, cost, rarity)
        if not isinstance(defense, int):
            raise ValueError("Error: Defense value has to be a integer")
        if not isinstance(damage, int):
            raise ValueError("Error: Damage value has to be a integer")

        if not isinstance(health, int):
            raise ValueError("Error: Health value has to be a integer")
        if not isinstance(defense, int):
            raise ValueError("Error: Defense value has to be a integer")
        self.damage = damage
        self.defense = defense
        self.id = id
        self.health = health
        self.rating = self.calculate_rating()
        self.wins = 0
        self.losses = 0
        self.rank = 0

    def calculate_rating(self) -> int:
        return self.cost * 70 + 1000 + self.health

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"rank": self.rank}

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

    def attack(self, target) -> dict:
        damage = max(0, self.damage - target.defense)
        target.health -= damage
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
        }

    def defend(self, incoming_damage: int) -> dict:
        try:
            incoming_damage + 0
        except TypeError:
            return {"Error": "Damage must be a number"}

        if self.defense < incoming_damage:
            damage_blocked = self.defense
        else:
            damage_blocked = incoming_damage
        damage_taken = incoming_damage - damage_blocked

        self.healty -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.healty > 0
            }

    def get_combat_stats(self) -> dict:
        return {"name": self.name,
                "health": self.health,
                "defense": self.defense,
                "damage": self.damage
                }

    def get_tournament_stats(self) -> dict:
        return {"name": self.name,
                "id": self.id,
                "wins": self.wins,
                "losses": self.losses,
                "health": self.health,
                "defense": self.defense,
                "damage": self.damage
                }
