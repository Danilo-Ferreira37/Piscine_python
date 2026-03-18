import sys
import importlib


class DependenceNotInstalled(Exception):
    pass


def check_packets(packet: str, info: str) -> bool:
    try:
        module = importlib.import_module(packet)
        print(f"[OK] {packet} ({module.__version__}) - {info}")
        return True
    except ModuleNotFoundError:
        print(f"[KO] {packet} - Module don't installed")
        return False


def installation_tutorial() -> None:
    print("\nFor pip intallation enter:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate")
    print("pip install -r requirements.txt")
    print("Then executes the file again:\npython3 loading.py")
    print("\nFor exit of virtual envinroment enter: deactivate\n")

    print("For Poetry installation enter:")
    print("curl -sSL https://install.python-poetry.org | python3 -")
    print("poetry install")
    print("Then executes:\npoetry run python loading.py")


def analise():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame({"matrix_values": data})

    print("Generating visualization...")
    plt.hist(df["matrix_values"], bins=30, color="red", alpha=0.7)
    plt.title("Matrix Data Distribution")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    output = "matrix_analysis.png"
    plt.savefig(output)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    verify = True
    packets = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
        "numpy": "Numerical computation ready"
        }
    pacs = []

    for pac, info in packets.items():
        try:
            if not check_packets(pac, info):
                raise DependenceNotInstalled()
        except DependenceNotInstalled:
            pacs.append(pac)
            verify = False

    if not verify:
        print(f"\nThe packages{pacs} are not installed.")
        installation_tutorial()
        return

    analise()
    exe = sys.executable
    if "poetry" in exe:
        print("Environment: Poetry virtualenv detected")
    elif "matrix_env" in exe:
        print("Environment: pip virtualenv detected")
    else:
        print("Environment: system Python (not recommended)")


if __name__ == "__main__":
    main()
