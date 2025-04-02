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

    success_flag = False
    while not success_flag:
        print(f"Starting hack automation...")
        hack.open_game_guardian()  # Open Game Guardian overlay
        hack.select_process()  # Select DragonVale process
        hack.select_search_tab()  # Select search tab
        hack.click_search_button()  # Select search button
        if hack.get_copy_value() != item_value: # Check if existing value is already set to item value
            hack.enter_qword_value(item_value)  # Press each key to search for item value
        hack.select_qword_search_type()  # Change search type
        hack.search()  # Click search button
        hack.click_change_all_values_button()  # Click on the change all values button
        if resource == "DragonCash":
            hack.enter_qword_value(-resource_value)  # For DragonCash, directly set the value to the desired amount
        else:
            hack.enter_qword_value(0)  # Press each key to change value to 0
            hack.click_yes_button()  # Click yes button
            hack.click_first_result()  # Click on the first result (Galaxy Flag)
            hack.goto()  # Go to the resource value
            hack.arrow_down(resource_skips + 1)  # Skip to the resource value
            hack.press_key("enter")  # Press enter to select the resource value
            hack.move_and_click(700, 740, sleep=0.5)  # Select Q-Word type
            hack.enter_qword_value(-resource_value)  # Press each key to change value to the desired amount
        hack.click_yes_button()  # Click yes button
        hack.close_game_guardian()  # Close Game Guardian overlay
        hack.move_and_click(1350, 950, sleep=1.5) # Buy another Galaxy Flag with the hacked resources
        hack.move_and_click(1550, 950)  # Place the Galaxy Flag in the free slot
        print("hack automation complete\n")

        if resource == "DragonCash":
            break  # For DragonCash, we can return immediately after setting the value

        success_flag = get_success_flag()  # Ask if the hack was successful
        if not success_flag:
            print("Retrying hack...\n")
            time.sleep(2)


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Resource Hack...\n")
        main()
    except Exception:
        print(f"Resource Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Resource Hack executed in {END - START:.2f} seconds")