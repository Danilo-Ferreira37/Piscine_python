import sys
import os
import site


def is_venv() -> bool:
    return (sys.prefix != sys.base_prefix)


def main() -> None:
    if is_venv():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")

        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix.env\nScripts\nactivate    #On Windows\n")

        print("Then run this program again.")


if "__main__" == __name__:
    main()
