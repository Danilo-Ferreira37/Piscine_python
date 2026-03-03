import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}\n")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for av in range(1, len(sys.argv)):
            print(f"Argument {av}: {sys.argv[av]}")
        print(f"Total arguments: {len(sys.argv)}")
