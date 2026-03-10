from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, healty, damage, combate_type, mana):
        try:
            super().__init__(name, cost, rarity)
            if not damage > 0:
                raise ValueError("Damage has to be positive")
            if not healty > 0:
                raise ValueError("Healty has to be positive")    
            if not mana > 0:
                raise ValueError("Healty has to be positive")

            self.damage = damage
            self.healty = healty
            self.mana = mana
            self.combat_type = combate_type
            self.defense = 15
    

        except ValueError as e:
            print(e)
        except TypeError:
            print("The healty, damage and mana has to be a integer or a float")

    def play(self, game_state) -> dict:
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
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type}

    def defend(self, incoming_damage):
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

    def get_combat_stats(self):
        return {'name': self.name, 'defense': self.defense, 'health': self.healty}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        self.mana -= mana_used
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_used
            }

    def channel_mana(self, amount):
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}
    
    def get_magic_stats(self):
        return {'name': self.name, 'mana': self.mana}
