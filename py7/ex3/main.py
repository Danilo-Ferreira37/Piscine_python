from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
 

def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    fantasy_fact = FantasyCardFactory()
    agressive = AgressiveStrategy()
    game = GameEngine()
    game.configure_engine(fantasy_fact, agressive)
    game.simulate_turn()

    print(f"\nGame Report:\n{game.get_engine_status()}")

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")

if __name__ == "__main__":
    main()
    
