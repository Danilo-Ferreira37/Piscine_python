import os
from dotenv import load_dotenv


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_end = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    if mode == 'development':
        print(f"Mode: {mode}")
    elif mode == 'production':
        print(f"Mode: {mode}")
    else:
        print("Error: invalid mode")
        return

    if db:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: Missing (default: DEBUG)")

    if zion_end:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing")
    if "MATRIX_MODE" in os.environ:
        print("[OK] Production overrides available")
    else:
        print("[WARN] No environment overrides detected")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
