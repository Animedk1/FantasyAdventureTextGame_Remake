from backend import startMenu
import traceback
import sys

def main():
    startMenu()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_message = traceback.format_exc()
        print("\n\u001b[31mAn unexpected error occurred:\u001b[0m\n")
        print(error_message)

        # Log to file
        with open("error.log", "w") as f:
            f.write(error_message)

        input("\n\u001b[33mPress Enter to exit...\u001b[0m")
        sys.exit(1)
