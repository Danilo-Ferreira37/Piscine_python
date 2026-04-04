def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda art: art['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f" * {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {'max_power': max(mages, key=lambda m: m['power']),
            'min_power': min(mages, key=lambda m: m['power']),
            'avg_power': sum(map(lambda m: m["power"], mages)) / len(mages)}


def main() -> None:
    try:
        print("\nTesting artifact sorter...")
        artifacts = [{'name': 'Crystal Orb', 'power': 85, 'type': 'heal'},
                     {'name': 'Fire Staff', 'power': 92, 'type': 'fireball'}]
        new_artifc = sorted(artifacts, key=lambda p: p["power"], reverse=True)
        print(f"{new_artifc[0]['name']} ({new_artifc[0]['power']} power) "
              "comes "
              f"before {new_artifc[1]['name']} ({new_artifc[1]['power']}"
              " power)")

        print("\nTesting spell transformer...")
        spells = ["fireball", "heal", "shield"]
        new_spells = spell_transformer(spells)
        for s in new_spells:
            print(s, end=" ")
        print()
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(f"Error: The keyword has to be {e}")
    except IndexError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
