import os, sys
from dotenv import load_dotenv

def main():
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: ")
    print(f"Database: ")
    print("")



if __name__ == "__main__":
    main()
