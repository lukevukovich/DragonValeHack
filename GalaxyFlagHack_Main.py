import traceback
import time
from src.DragonValeHack import DragonValeHack

"""
Galaxy Flag Hack Script:
    This script automates the process of buying a galaxy flag for free in DragonVale.

Prerequisites:
    - Ensure Nox is fullscreen windowed (for accurate coordinates)
    - Ensure DragonVale is running
    - Ensure screen is on free slot (to place the flag)
    - Ensure Game Guardian is running and DragonVale process selected
"""


def main():
    """
    Main function to execute the Galaxy Flag Hack script.
    """
    hack = DragonValeHack()

    hack.move_and_click(1750, 950, sleep=2)  # Open market
    hack.move_and_click(450, 800, sleep=3)  # Select decorations
    hack.move_and_click(1200, 80, sleep=1)  # Select search bar
    hack.move_and_click(900, 500, sleep=0.1)  # Click in search bar to start typing
    hack.type("galaxy", interval=0.2)  # Type "galaxy" in the search bar
    hack.move_and_click(1340, 600, sleep=0.5) # Search button
    hack.move_and_click(350, 540, sleep=0.5)  # Click on the first result (Galaxy Flag)
    hack.open_game_guardian()  # Open Game Guardian overlay
    hack.click_search_button()  # Select search button
    hack.enter_qword_value(2191473)  # Press each key to search for 2,191,473
    hack.select_qword_search_type()  # Change search type
    hack.search() # Click search button
    hack.move_and_click(1650, 230, sleep=0.5)  # Select change all values button
    hack.move_and_click(1410, 550, sleep=0.8)  # Change value to 0 (to get it for free)
    hack.click_ok_button()  # Click OK button
    hack.close_game_guardian()  # Close Game Guardian overlay
    hack.move_and_click(1540, 220, sleep=0.5)  # Close selected item
    hack.click_first_result()  # Click on the first result (Galaxy Flag)
    hack.move_and_click(1150, 900, sleep=1.5)  # Buy the Galaxy Flag for free
    hack.move_and_click(1550, 950)  # Place the Galaxy Flag in the free slot


if __name__ == "__main__":
    START = time.time()

    try:
        print("Starting Galaxy Flag Hack...")
        main()
    except Exception:
        print(f"Galaxy Flag Hack error: {traceback.format_exc()}")

    END = time.time()
    print(f"Galaxy Flag Hack executed in {END - START:.2f} seconds")