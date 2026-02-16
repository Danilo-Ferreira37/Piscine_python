def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    line1 = "[ENTRY 001] New quantum algorithm discovered\n"
    line2 = "[ENTRY 002] Efficiency increased by 347%\n"
    line3 = "[ENTRY 003] Archived by Data Archivist trainee\n"
    with open("new_discovery.txt", "w") as new_file:
        print(f"Initializing new storage unit: {new_file.name}")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        new_file.write(line1)
        new_file.write(line2)
        new_file.write(line3)
        print(line1, end="")
        print(line2, end="")
        print(line3, end="")
        print("\nData inscription complete. Storage unit sealed")
        print(f"Archive '{new_file.name}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
