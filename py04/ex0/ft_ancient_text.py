
def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        with open("ancient_fragment.txt") as file:
            print(f"Accessing Storage Vault: {file.name}")
            print("Connection established...\n")
            print(file.read())
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    
if __name__ == "__main__":
    main()
