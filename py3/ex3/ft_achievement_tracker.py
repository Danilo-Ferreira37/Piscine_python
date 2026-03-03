if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    }
    for player in players:
        print(f"Player {player} achievements: {players[player]}")

    print("\n=== Achievement Analytics ===")
    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(players[player])
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common = set(players["alice"])
    for player_achieve in players:
        common = common.intersection(players[player_achieve])
    print(f"\nCommon to all players: {common}")

    rare = set()
    for player in players:
        unique = set(players[player])
        for other in players:
            if other != player:
                unique = unique.difference(players[other])
        rare = rare.union(unique)
    print(f"Rare achievements (1 player): {rare}\n")

    common = set(players["alice"])
    common = common.intersection(players["bob"])
    dif = set(players["alice"])
    dif = dif.difference(players["bob"])
    print(f"Alice vs Bob common: {common}")
    print(f"Alice unique: {dif}")
    dif = set(players["bob"])
    dif = dif.difference(players["alice"])
    print(f"Bob unique: {dif}")
