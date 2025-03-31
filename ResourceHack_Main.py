import traceback
import time
from src.DragonValeHack import DragonValeHack
import subprocess

"""
Resource Hack Script:
    This script automates the process of hacking resources in DragonVale.

Prerequisites:
    - Ensure Nox is fullscreen windowed (for accurate coordinates)
    - Ensure DragonVale is running
    - Ensure galaxy flag is selected
    - Ensure Game Guardian is running and DragonVale process selected

Resources:
    - DragonCash
    - EXP
    - Food
    - Gems
    - Event Currency
    - Wishes
    - Eternal essence
    - Abundant essence
    - Vital essence
    - Ethereum
"""

# Resource mapping for resource and number of data entries to skip
RESOURCE_MAPPING = {
    "DragonCash": 0,
    "EXP": 2,
    "Food": 4,
    "Gems": 6,
    "Event Currency": 10,
    "Wishes": 12,
    "Eternal essence": 16,
    "Abundant essence": 18,
    "Vital essence": 20,
    "Ethereum": 22
}


def get_resource() -> str:
    """
    Get the resource to hack from the user.

    Returns:
        str: The selected resource.
    """
    while True:
        for i, resource in enumerate(RESOURCE_MAPPING.keys()):
            print(f"{i + 1}. {resource}")
        try:
            choice = int(input("Select the resource to hack (1-10): ")) - 1
            if 0 <= choice < len(RESOURCE_MAPPING):
                choice_str = list(RESOURCE_MAPPING.keys())[choice]
                return choice_str
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(RESOURCE_MAPPING)}.")
                time.sleep(2)
                subprocess.run("cls", shell=True)
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(2)
            subprocess.run("cls", shell=True)


def get_resource_value(resource: str) -> int:
    """
    Get the resource value to hack from the user.
    """
    while True:
        try:
            value = int(input(f"Enter desired amount of {resource}: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(2)
            subprocess.run("cls", shell=True)


def get_success_flag() -> bool:
    """
    Get the success flag from the user.

    Returns:
        bool: True if the hack was successful, False otherwise.
    """
    while True:
        try:
            choice = input("Was the hack successful? (y/n): ").strip().lower()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    """
    Main function to execute the Resource Hack script.
    """
    resource = get_resource()
    resource_skips = RESOURCE_MAPPING[resource]
    resource_value = get_resource_value(resource)
    print(f"Hacking {resource} with value {resource_value}")

    hack = DragonValeHack()
    print("\nInitialized DragonValeHack instance")

    success_flag = False
    while not success_flag:
        print(f"Starting hack automation...")
        hack.open_game_guardian()  # Open Game Guardian overlay
        hack.select_process()  # Select DragonVale process
        hack.select_search_tab()  # Select search tab
        hack.click_search_button()  # Select search button
        hack.enter_qword_value(2191473)  # Press each key to search for 2,191,473
        hack.select_qword_search_type()  # Change search type
        hack.search()  # Click search button
        hack.click_change_all_values_button()  # Click on the change all values button
        hack.enter_qword_value(0)  # Press each key to change value to 0
        hack.click_yes_button()  # Click yes button
        hack.click_first_result()  # Click on the first result (Galaxy Flag)
        hack.goto()  # Go to the resource value
        hack.arrow_down(resource_skips + 1)  # Skip to the resource value
        hack.press_key("enter")  # Press enter to select the resource value
        hack.move_and_click(700, 740, sleep=0.5)  # Click on the value to edit it
        hack.enter_qword_value(-resource_value)  # Press each key to change value to the desired amount
        hack.click_yes_button()  # Click yes button
        hack.close_game_guardian()  # Close Game Guardian overlay
        hack.move_and_click(1350, 950, sleep=1.5) # Buy another Galaxy Flag with the hacked resources
        hack.move_and_click(1550, 950)  # Place the Galaxy Flag in the free slot
        print("hack automation complete\n")

        success_flag = get_success_flag()  # Ask if the hack was successful
        if not success_flag:
            print("Retrying hack...\n")
            time.sleep(2)


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Resource Hack Hack...\n")
        main()
    except Exception:
        print(f"Resource Hack Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Resource Hack Hack executed in {END - START:.2f} seconds")