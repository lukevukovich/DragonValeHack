import traceback
import time
from src.DragonValeHack import DragonValeHack
from src.DragonValeHack_Util import *

"""
Multi Resource Hack Script:
    This script automates the process of hacking multiple resources (through one sale) in DragonVale. Supports 1080p resolution.

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


def hack_resources(hack: DragonValeHack, resource_mapping: dict) -> None:
    """
    Iteratively hack each resource in the provided mapping.

    Args:
        resource_mapping (dict): A dictionary containing the resources to hack and their corresponding values.
    """
    skip_count = 0
    resource_skips = [resource_dict["skips"] for _, resource_dict in resource_mapping.items()]
    reversed_resource_mapping = {v: k for k, v in RESOURCE_MAPPING.items()} # Reverse the original mapping to get the resource names from skips
    while True:
        if skip_count in resource_skips:
            resource = reversed_resource_mapping[skip_count]  # Get the resource name from the skip count
            resource_dict = resource_mapping[resource]  # Get the dictionary for the current resource
            resource_value = resource_dict["value"]  # Get the value of the resource to hack
            hack.press_key("enter")  # Press enter to select the resource value
            hack.move_and_click(700, 740, sleep=0.5)  # Select Q-Word type
            hack.enter_qword_value(-resource_value)  # Press each key to change value to the desired amount
            hack.click_yes_button()  # Click yes button
            hack.arrow_down() # Reposition selection
            print(f"Hacked {resource_value} {resource}")

        if skip_count >= resource_skips[-1]:  # If we've processed all resources in the mapping, exit the loop
            break

        hack.arrow_down() # Move down to the next resource in the list
        skip_count += 1


def main():
    """
    Main function to execute the Multi Resource Hack script.
    """
    resource_mapping = get_resources()  # Get the value of each desired resource from user
    item = get_item()  # Get the item to hack from the user
    item_value = ITEM_MAPPING[item]  # Get the corresponding Q-Word value for the selected item
    print(f"Hacking resources from item {item.title()}")

    hack = DragonValeHack()
    print("\nInitialized DragonValeHack instance")

    success_flag = False
    while not success_flag:
        print(f"Starting hack automation...")
        hack.open_game_guardian()  # Open Game Guardian overlay
        hack.select_process()  # Select DragonVale process
        hack.select_search_tab()  # Select search tab
        hack.click_search_button()  # Select search button
        print(hack.get_copy_value(), item_value) # Debug: Print the current copied value from the search box
        if hack.get_copy_value() != item_value: # Check if existing value is already set to item value
            hack.enter_qword_value(item_value)  # Press each key to search for item value
        hack.select_qword_search_type()  # Change search type
        hack.search()  # Click search button
        hack.click_change_all_values_button()  # Click on the change all values button
        hack.enter_qword_value(0)  # Press each key to change value to 0
        hack.click_yes_button()  # Click yes button
        hack.click_first_result()  # Click on the first result (Galaxy Flag)
        hack.goto()  # Go to the resource value
        hack.arrow_down() # Move down to correct position
        hack_resources(hack, resource_mapping)  # Hack each resource in the mapping
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
        print("Starting Multi Resource Hack...\n")
        main()
    except Exception:
        print(f"Multi Resource Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Multi Resource Hack executed in {END - START:.2f} seconds")