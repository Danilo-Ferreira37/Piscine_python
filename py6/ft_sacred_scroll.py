import alchemy 


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_water(): alchemy.create_water()")

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError as e:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("Package metadata:")
    print(alchemy.__version__, "\n", alchemy.__author__ end)
if __name__ == "__main__":
    main()
