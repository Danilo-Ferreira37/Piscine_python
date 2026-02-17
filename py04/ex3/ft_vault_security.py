def main() -> None:
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ==\n")
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        with open("classified_data.txt", "r") as f:
            print("SECURE EXTRATION:")
            print(f.read())
        with open("vault.txt", "w") as f:
            print("\nSECURE PRESERVATION:")
            f.write("[CLASSIFIED] New security protocols archived")
        with open("vault.txt", "r") as f:
            print(f.read())
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security")
    except FileNotFoundError as e:
        print(f"Error: Do not found the file '{e.filename}'")


if __name__ == "__main__":
    main()
