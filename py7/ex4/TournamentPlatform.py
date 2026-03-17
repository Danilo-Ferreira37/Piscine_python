from ex4.TournamentCard import TournamentCard
import random

class TournamentPlataform():
    def __init__(self) -> None:
        self.cards = []
        self.total_cards = 0
        self.t_match = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        self.total_cards += 1
        interfaces = [cls.__name__ for cls in card.__class__.__bases__]
        print(f"{card.name} (ID: {card.id})")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card.rating}")
        print("- Record: 0-0\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        player1 = None
        player2 = None
        winner = None
        loser = None
        self.t_match += 1
        size = 0

        if card1_id == card2_id:
            raise ValueError("Error: The cards_id has to be diferrents!")
        for card in self.cards:
            size += 1
            if card.id == card1_id:
                player1 = card
            if card.id == card2_id:
                player2 = card
        if player1 == None or player2 == None:
            raise ValueError("Error: ID don't found!")
        if size < 2:
            raise ValueError("Error: Not suficient cards regitred")
        
        while True:
            player1.attack(player2)
            if player2.health <= 0:
                winner = player1
                player1.update_wins(1)
                player2.update_losses(1)
                loser = player2
                player1.rating += 10
                break

            player2.attack(player1)
            if player1.health <= 0:
                winner = player2
                player2.update_wins(1)
                player1.update_losses(1)
                loser = player1
                player2.rating += 10
                break

        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
            }

    def get_leaderboard(self) -> list:
        pos = 1
        ordenados = sorted(self.cards, key=lambda obj: obj.rating, reverse=True)
        output = []

        for card in ordenados:
            output.append(f"{pos}. {card.name} - Rating: {card.rating} ({card.wins} - {card.losses})")
            card.rank = pos
            pos += 1
        
        return output

    def generate_tournament_report(self) -> dict:
        avg = 0
        for c in self.cards:
            avg += c.rating
        
        try:
            avg / self.total_cards
        except ZeroDivisionError:
            avg = 0
        return {'total_cards': self.total_cards,
                'matches_played': self.t_match,
                'avg_rating': avg,
                'platform_status': 'active'
                }         
