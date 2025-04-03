import traceback
import time
from src.DragonValeHack import DragonValeHack
from src.DragonValeHack_Util import *

"""
Resource Hack Script:
    This script automates the process of hacking a resource in DragonVale. Supports 1080p resolution.

Prerequisites:
    - Ensure Nox is fullscreen windowed (for accurate coordinates)
    - Ensure DragonVale is running
    - Ensure Game Guardian is running
    - Ensure item is selected (Galaxy Flag, Mini Moss Rock, etc.)

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


def main():
    """
    Main function to execute the Resource Hack script.
    """
    resource = get_resource() # Get the resource to hack from the user
    resource_skips = RESOURCE_MAPPING[resource] # Get the number of skips for the resource
    resource_value = get_resource_value(resource) # Get the value to hack for the selected resource
    item = get_item()  # Get the item to hack from the user
    item_value = ITEM_MAPPING[item]  # Get the corresponding Q-Word value for the selected item
    print(f"Hacking {resource_value} {resource} from item {item.title()}")

    hack = DragonValeHack()
    print("\nInitialized DragonValeHack instance")

    print(f"Starting hack automation...")
    hack.open_game_guardian()  # Open Game Guardian overlay
    hack.select_process()  # Select DragonVale process
    hack.select_search_tab()  # Select search tab
    hack.click_search_button()  # Select search button
    if hack.get_copy_value() != str(item_value): # Check if existing value is already set to item value
        hack.enter_qword_value(item_value)  # Press each key to search for item value
        hack.select_qword_search_type()  # Change search type
    hack.search()  # Click search button
    hack.click_change_all_values_button()  # Click on the change all values button
    if resource == "DragonCash":
        hack.enter_qword_value(-resource_value)  # For DragonCash, directly set the value to the desired amount
        hack.click_yes_button()  # Click yes button
        print(f"Hacked {resource_value} DragonCash")
    else:
        hack.enter_qword_value(0)  # Press each key to change value to 0
        hack.click_yes_button()  # Click yes button

        entries = get_num_entries()  # Get the number of entries
        hack.select_search_tab()  # Select search tab
        if entries == 0:
            print("No entries found, quitting hack...\n")
            hack.close_game_guardian()  # Close Game Guardian overlay
            return
        elif entries > 8:
            print(f"Too many entries ({entries}), quitting hack...\n")
            hack.close_game_guardian() # Close Game Guardian overlay
            return

        for i in range(entries):
            print(f"\nHacking entry {i + 1} of {entries}...")
            hack.click_result(i + 1) # Click on the result
            hack.goto()  # Go to the resource value
            hack.arrow("down", resource_skips + 1)  # Skip to the resource value
            hack.press_key("enter")  # Press enter to select the resource value
            hack.move_and_click(700, 740, sleep=0.5)  # Select Q-Word type
            if resource != "DragonCash" and hack.get_copy_value() != "0":
                print(f"Bad entry detected, skipping")
                [hack.select_search_tab() for _ in range(2)]
                continue
            hack.enter_qword_value(-resource_value)  # Press each key to change value to the desired amount
            hack.click_yes_button()  # Click yes button
            hack.select_search_tab()  # Select search tab
            print(f"Hacked {resource_value} {resource}")

    hack.close_game_guardian()  # Close Game Guardian overlay
    hack.move_and_click(1350, 950, sleep=1.5) # Buy another Galaxy Flag with the hacked resources
    hack.move_and_click(1550, 950)  # Place the Galaxy Flag in the free slot
    print("hack automation complete\n")


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Resource Hack...\n")
        main()
    except Exception:
        print(f"Resource Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Resource Hack executed in {END - START:.2f} seconds")