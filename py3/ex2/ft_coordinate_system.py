import sys
import math


def parsing_coordinate(p1: tuple, p2: tuple):
    try:
        size = 0
        for arg in p2:
            int(arg)
            size += 1
        if size != 3:
            raise Exception("Number of arguments invalid")
        print(f"Distance between (0, 0, 0) and {p2}:"
              f" {distance_3d(p1, p2):.2f}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: ({e})")
    except Exception as e:
        print(e)


def distance_3d(p1: tuple, p2: tuple) -> int:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    x = (x2 - x1)**2
    y = (y2 - y1)**2
    z = (z2 - z1)**2

    return math.sqrt(x + y + z)


def main() -> None:
    p2 = ()
    size = 0
    try:
        for arg in sys.argv[1:]:
            p2 += int(arg),
            size += 1
        if size != 3:
            raise Exception("Error: Number of arguments is invalid")
    except ValueError as e:
        print(f"Parsing invalid cordinates: {sys.argv[1:]}")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: ({e})")
        return
    except Exception as e:
        print(e)
        return

    p1 = (0, 0, 0)
    print(f"Position created: {p2}")
    parsing_coordinate(p1, p2)

    p2 = (3, 4, 0)
    print("Parsing coordinates: \"3,4,0\"")
    print(f"Parsed position: {p2}")
    parsing_coordinate(p1, p2)

    p2 = ("abc", "def", "ghi")
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    parsing_coordinate(p1, p2)

    print("\nUnpacking demonstration: ")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()
