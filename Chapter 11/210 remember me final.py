
import subprocess
import sys


def run_command(description, command_list):
    """Run a system command and print output in a clean format."""
    print(f"\n--- {description} ---")
    try:
        result = subprocess.run(
            command_list, text=True, capture_output=True, check=False
        )
        print(result.stdout)
        if result.stderr:
            print("Errors / Warnings:")
            print(result.stderr)
    except Exception as e:
        print(f"Could not run command: {e}")


def show_page_210_instructions():
    """Print the book's instructions exactly as Page 210 explains them."""
    print("\n=== PYTHON CRASH COURSE – PAGE 210 INSTRUCTIONS ===")
    print("To update pip manually using your terminal, run:")
    print("\n    python -m pip install --upgrade pip\n")
    print("To update any other third‑party package, use:")
    print("\n    python -m pip install --upgrade package_name\n")
    print("NOTE: On Linux systems, pip may not be preinstalled.")


def main():
    print(">>> Chapter 11 – Page 210 Helper Script <<<")

     Show your current pip version
    run_command(
        "Checking current pip version",
        [sys.executable, "-m", "pip", "--version"]
    )

     Attempt pip upgrade
    run_command(
        "Attempting to upgrade pip (same as the book's example)",
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
    )

    Print book instructions for clarity
    show_page_210_instructions()


if __name__ == "__main__":
    main()
