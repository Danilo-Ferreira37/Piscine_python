def garden_operations() -> None:
    try:
        int("oitenta")
    except ValueError as e:
        print(f"Testing {type(e).__name__}...")
        print(f"Caught {type(e).__name__}: invalid literal for int()\n")

    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Testing {type(e).__name__}...")
        print(f"Caught {type(e).__name__}: {e}\n")

    try:
        open("danilinho")
    except FileNotFoundError as e:
        print(f"Testing {type(e).__name__}")
        print(f"Caught {type(e).__name__}: No such file {e.filename}\n")

    try:
        data = {"danilo": "age = 90"}
        print(data["plant"])
    except KeyError as e:
        print(f"Testing {type(e).__name__}...")
        print(f"Caught {type(e).__name__}: 'missing_{e.args[0]}'\n")

    try:
        int("abc")
    except (ValueError, ZeroDivisionError) as e:
        print("Testing multiple errors together...")
        print(f"Caught an error, but program continues!\n")

def test_error_types() -> None:
    garden_operations()
    print("All error types tested successfully!")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
