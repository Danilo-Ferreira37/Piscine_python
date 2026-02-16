import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {status}")
    sys.stderr.write("\n[ALERT] System diagnostic: Communication channels verified")
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
