from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlataform
from ex0.Card import Rarity


def main() -> None:
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        card1 = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY,
                               7, 100, 4, "dragon_001")
        card2 = TournamentCard("Ice Wizard", 5, Rarity.RARE,
                               3, 3, 6, "wizard_001")
        tournament = TournamentPlataform()
        tournament.register_card(card1)
        tournament.register_card(card2)

        print("Creating tournament match...")
        print(f"Match result: {tournament.create_match(card1.id, card2.id)}\n")
        print("Tournament Leaderboard:")
        bourd = tournament.get_leaderboard()
        for player in bourd:
            print(player)

        print(f"\nPlatform Report:\n{tournament.generate_tournament_report()}")
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
