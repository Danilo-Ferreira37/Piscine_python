if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = [ 
        {"name": "alice", "score": 2300, "active": True},
        {"name": "bob", "score": 1800, "active": True},
        {"name": "charlie", "score": 2150, "active": True},
        {"name": "diana", "score": 2050, "active": False}
    ]
    hight_scores = [n["name"] for n in players if n["score"] > 2000]
    scores_doubles = [s["score"] * 2 for s in players]
    active_players = [a["name"] for a in players if a["active"]]
    print(f"Hight scores (>2000): {hight_scores}")
    print(f"Scores doubled: {scores_doubles}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    players = [
        {"name": "alice", "score": 2300, "achievements": 5},
        {"name": "bob", "score": 1800, "achievements": 3},
        {"name": "charlie", "score": 2150, "achievements": 7}
    ]
    categories = {'high': 3, 'medium': 2, 'low': 1}

    player_scores = {p["name"]: p["score"] for p in players}
    categories = {c: v for c, v in categories.items()}
    achieves = {ac["name"]: ac["achievements"] for ac in players}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {achieves}")

    print("\n=== Set Comprehension Examples ===")
    players = [
        {"name": "alice", "region": "north", "achievements": "boss_slayer"},
        {"name": "bob", "region": "east", "achievements": "level_10"},
        {"name": "charlie", "region": "central", "achievements": "first_kill"},
        {"name": "alice", "region": "east", "achievements": "level_10"}
    ]
    regions = {"west": False, "north": True, "north": True, "east": True, "south": False, "central": True}
    uni_players = {n["name"] for n in players}
    uni_achieve = {n["achievements"] for n in players}
    uni_regions ={r for r in regions if regions[r]}
    print(f"Unique players: {uni_players}")
    print(f"Unique achievements: {uni_achieve}")
    print(f"Active regions: {uni_regions}")

    players = [
        {"name": "alice", "score": 2300, "achievements": 5},
        {"name": "bob", "score": 1800, "achievements": 3},
        {"name": "charlie", "score": 2150, "achievements": 7}
    ]
    scores = {p["score"] for p in players}
    more_score = max(scores)
    top_play = [p["name"] for p in players if p["score"] == more_score][0]
    top_achieve = [p["achievements"] for p in players if p["score"] == more_score][0]

    print("\n ===Combined Analysis ===")
    print(f"Total players {len(uni_players)}")
    print(f"Total unique achievements: {len(achieves)}")
    print(f"Average score: {sum(scores_doubles) / 2 / len(uni_players):.1f}")
    print(f"Top performer: {top_play} ({more_score} points, {top_achieve} achievements)")
