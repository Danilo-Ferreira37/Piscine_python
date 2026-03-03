import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    lyst = []
    total = len(sys.argv)
    try:
        if total < 2:
            raise Exception("No scores provided. Usage: python3 ft_score_"
                            "analytics.py <score1> <score2> ...")
        for arg in sys.argv[1:]:
            lyst += [int(arg)]
        print(f"Scores processed: {lyst}")
        print(f"Total players: {total - 1}")
        print(f"Total score: {sum(lyst)}")
        print(f"Average score: {sum(lyst) / (total - 1):.1f}")
        print(f"High score: {max(lyst)}")
        print(f"Low score: {min(lyst)}")
        print(f"Score range {max(lyst) - min(lyst)}")

    except ValueError:
        print(f"The score: '{arg}' is invalid. The score has to be a number")
    except Exception as e:
        print(e)
