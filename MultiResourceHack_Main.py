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


def hack_resources(hack: DragonValeHack, resource_mapping: dict, add_or_remove: str) -> None:
    """
    Iteratively hack each resource in the provided mapping.

    Args:
        resource_mapping (dict): A dictionary containing the resources to hack and their corresponding values.
        add_or_remove (str): A string indicating whether to add or remove the resource value.
    """
    skip_count = 0
    resource_skips = [resource_dict["skips"] for _, resource_dict in resource_mapping.items()]
    reversed_resource_mapping = {v: k for k, v in RESOURCE_MAPPING.items()} # Reverse the original mapping to get the resource names from skips
    while True:
        if skip_count in resource_skips:
            resource = reversed_resource_mapping[skip_count]  # Get the resource name from the skip count
            resource_dict = resource_mapping[resource]  # Get the dictionary for the current resource
            resource_value = resource_dict["value"]  # Get the value of the resource to hack
            hack.press_key("enter", sleep=0.7)  # Press enter to select the resource value
            hack.move_and_click(700, 740, sleep=0.6)  # Select Q-Word type
            if resource != "DragonCash" and hack.get_copy_value() != "0":
                print(f"Bad entry detected, skipping")
                hack.select_search_tab()  # Click off item
                return # If the copied value is not 0, exit the function
            hack.enter_qword_value(-resource_value if add_or_remove == "add" else resource_value)  # Press each key to change value to the desired amount
            hack.click_yes_button()  # Click yes button
            hack.arrow("down") # Reposition selection
            print(f"{"Added" if add_or_remove == "add" else "Removed"} {resource_value} {resource}")

        if skip_count >= resource_skips[-1]:  # If we've processed all resources in the mapping, exit the loop
            break

        hack.arrow("down") # Move down to the next resource in the list
        skip_count += 1


def main():
    """
    Main function to execute the Multi Resource Hack script.
    """
    resource_mapping = get_resources()  # Get the value of each desired resource from user
    add_or_remove = get_add_or_remove()  # Get whether to add or remove the item
    item = get_item()  # Get the item to hack from the user
    item_value = ITEM_MAPPING[item]  # Get the corresponding Q-Word value for the selected item
    print(f"Hacking resources from {item.title()}")

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
    hack.wait(1)  # Wait for a second
    hack.click_change_all_values_button()  # Click on the change all values button
    if list(resource_mapping.keys()) == ["DragonCash"]: # If only DragonCash is selected, set the value directly
        value = resource_mapping["DragonCash"]["value"] # Get the value of DragonCash to hack
        hack.enter_qword_value(-value if add_or_remove == "add" else value) # For DragonCash, directly set the value to the desired amount
        hack.click_yes_button()  # Click yes button
        print(f"{"Added" if add_or_remove == "add" else "Removed"} {value} DragonCash")
    else:
        hack.wait(0.5)  # Wait for half a second
        hack.enter_qword_value(0)  # Press each key to change value to 0
        hack.click_yes_button()  # Click yes button

        hack.select_search_tab()  # Select search tab
        entries = hack.detect_num_entries()  # Detect the number of entries
        if entries == 0:
            print("\nNo entries found, quitting hack...\n")
            hack.close_game_guardian()  # Close Game Guardian overlay
            return
        elif entries == 8:
            print(f"\nToo many entries ({entries}), quitting hack...\n")
            hack.close_game_guardian() # Close Game Guardian overlay
            return
        print(f"\nFound {entries} entries, proceeding with hack...")

        for i in range(entries):
            print(f"\nHacking entry {i + 1} of {entries}...")
            hack.click_result(i + 1) # Click on the result
            hack.wait(0.75)  # Wait
            hack.goto()  # Go to the resource value
            hack.arrow("down") # Move down to correct position
            hack_resources(hack, resource_mapping, add_or_remove)  # Hack each resource in the mapping
            hack.select_search_tab()  # Select search tab

    hack.close_game_guardian()  # Close Game Guardian overlay
    hack.move_and_click(1350, 950, sleep=1.2) # Buy another Galaxy Flag with the hacked resources
    if add_or_remove == "remove" and list(resource_mapping.keys()) != ["DragonCash"]:
        hack.move_and_click(730, 830, sleep=1.2) # If removing resource, click buy button to buy the item
    hack.move_and_click(1550, 950)  # Place the Galaxy Flag in the free slot
    print("\nHack automation complete")


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Multi Resource Hack...")
        main()
    except Exception:
        print(f"Multi Resource Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Multi Resource Hack executed in {END - START:.2f} seconds")