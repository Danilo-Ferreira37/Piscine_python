def error_handle(file: str) -> None:
    try:
        if file == "ancient_fragment.txt":
            with open(file) as f:
                f.write("hello guys")
        with open(file) as f:
            print(f"SUCCESS: Archive recovered - ''{f.read()}''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Fatal error '{f.name}' {e}")
        print("STATUS: Crisis handled, system it's fine\n")


def main() -> None:
    try:
        print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        error_handle("lost_archive.txt")

        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        error_handle("classified_vault.txt")

        print("CRISIS ALERT: Attempting access to 'ancient_fragment.txt'...")
        error_handle("ancient_fragment.txt")

        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        error_handle("standard_archive.txt")
    finally:
        print("All crisis scenarios handled successfully. Archives secure.")

if __name__ == "__main__":
    main()
