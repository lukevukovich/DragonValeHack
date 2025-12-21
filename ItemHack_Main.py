import traceback
import time
from src.DragonValeHack import DragonValeHack
from src.DragonValeHack_Util import *

"""
Item Hack Script:
    This script automates the process of buying a item for free in DragonVale. Supports 1080p resolution.

Prerequisites:
    - Ensure Nox is fullscreen windowed (for accurate coordinates)
    - Ensure DragonVale is running
    - Ensure Game Guardian is running
    - Ensure screen is on free slot (to place the item)

Items:
    - Galaxy Flag (level 11 and above)
    - Famed Flat Rock (below level 11)
"""


def main():
    """
    Main function to execute the Item Hack script.
    """
    item = get_item()  # Get the item to hack from the user
    item_value = ITEM_MAPPING[item] # Get the corresponding Q-Word value for the selected item
    print(f"Hacking {item.title()} with value {item_value}")

    hack = DragonValeHack()
    print("\nInitialized DragonValeHack instance")

    print(f"Starting hack automation...")
    hack.move_and_click(1750, 950, sleep=2)  # Open market
    hack.move_and_click(1450, 400, sleep=3)  # Select decorations
    hack.move_and_click(1200, 80, sleep=1)  # Select search bar
    hack.move_and_click(900, 500, sleep=0.1)  # Click in search bar to start typing
    hack.type(item, interval=0.2)  # Type item in the search bar
    hack.move_and_click(1340, 600, sleep=0.5) # Search button
    hack.move_and_click(350, 540, sleep=0.5)  # Click on the first result (selected item)
    hack.open_game_guardian()  # Open Game Guardian overlay
    hack.select_process()  # Select DragonVale process
    hack.select_search_tab()  # Select search tab
    hack.click_search_button()  # Select search button
    hack.wait(0.5)  # Wait
    if hack.get_copy_value() != str(item_value): # Check if existing value is already set to item value
        hack.enter_qword_value(item_value)  # Press each key to search for item value
        hack.select_qword_search_type()  # Change search type
    hack.search() # Click search button
    hack.wait(1)  # Wait
    hack.click_change_all_values_button()  # Click on the change all values button
    hack.enter_qword_value(0)  # Press each key to change value to 0
    hack.click_yes_button()  # Click yes button
    hack.close_game_guardian()  # Close Game Guardian overlay
    hack.move_and_click(1540, 220, sleep=0.5)  # Close selected item
    hack.click_first_result()  # Click on the first result (item)
    hack.move_and_click(1150, 900, sleep=1.5)  # Buy the item for free
    hack.move_and_click(1550, 950)  # Place the item in the free slot
    print("\nHack automation complete")


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Item Hack...")
        main()
    except Exception:
        print(f"Item Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Item Hack executed in {END - START:.2f} seconds")