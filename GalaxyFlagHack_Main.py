import pyautogui
import time

"""
Galaxy Flag Hack Script:
    This script automates the process of buying a galaxy flag for free in DragonVale.

Prerequisites:
    - Ensure Nox is fullscreen windowed (for accurate coordinates)
    - Ensure DragonVale is running
    - Ensure screen is on free slot (to place the flag)
    - Ensure Game Guardian is running and DragonVale process selected
"""

START = time.time()

# Open market
pyautogui.moveTo(1750, 950)
pyautogui.click()
time.sleep(2)

# Select decorations
pyautogui.moveTo(450, 800)
pyautogui.click()
time.sleep(3)

# Select search bar
pyautogui.moveTo(1200, 80)
pyautogui.click()
time.sleep(1)

# Click in search bar to start typing
pyautogui.moveTo(900, 500)
pyautogui.click()
time.sleep(0.1)

# Type "galaxy" in the search bar, search
pyautogui.typewrite("galaxy", interval=0.1)
pyautogui.moveTo(1340, 600)
pyautogui.click()

# Click on the first result (Galaxy Flag)
pyautogui.moveTo(350, 540)
pyautogui.click()
time.sleep(0.5)

# Open Game Guardian overlay
pyautogui.moveTo(70, 80)
pyautogui.click()
time.sleep(0.5)

# Select search button
pyautogui.moveTo(1730, 230)
pyautogui.click()
time.sleep(0.5)

# Press each key to search for 2,191,473
# 2
pyautogui.moveTo(1475, 275)
pyautogui.click()
time.sleep(0.5)

# 1
pyautogui.moveTo(1380, 275)
pyautogui.click()
time.sleep(0.5)

# 9
pyautogui.moveTo(1570, 450)
pyautogui.click()
time.sleep(0.5)

# 1
pyautogui.moveTo(1380, 275)
pyautogui.click()
time.sleep(0.5)

# 4
pyautogui.moveTo(1380, 360)
pyautogui.click()
time.sleep(0.5)

# 7
pyautogui.moveTo(1380, 450)
pyautogui.click()
time.sleep(0.5)

# 3
pyautogui.moveTo(1570, 275)
pyautogui.click()
time.sleep(0.5)

# Change search type
pyautogui.moveTo(700, 450)
pyautogui.click()
time.sleep(0.5)

# Select data type
pyautogui.moveTo(800, 700)
pyautogui.scroll(100)
pyautogui.scroll(100)
pyautogui.scroll(100)
time.sleep(0.5)
pyautogui.click()

# Try to click new search button (if it appears)
pyautogui.moveTo(260, 830)
pyautogui.click()
time.sleep(1)

# Click search button
pyautogui.moveTo(1600, 830)
pyautogui.click()
time.sleep(1)

# Select change all values button
pyautogui.moveTo(1650, 230)
pyautogui.click()
time.sleep(0.5)

# Change value to 0 (to get it for free)
pyautogui.moveTo(1410, 550)
pyautogui.click()
time.sleep(0.8)

# Click OK button
pyautogui.moveTo(1650, 830)
pyautogui.click()
time.sleep(0.2)

# Close Game Guardian overlay
pyautogui.moveTo(1815, 80)
pyautogui.click()

# Close selected item
pyautogui.moveTo(1540, 220)
pyautogui.click()
time.sleep(0.5)

# Click on the first result (Galaxy Flag)
pyautogui.moveTo(350, 540)
pyautogui.click()
time.sleep(0.5)

# Buy the Galaxy Flag for free
pyautogui.moveTo(1150, 900)
pyautogui.click()
time.sleep(1.5)

# Place the Galaxy Flag in the free slot
pyautogui.moveTo(1550, 950)
pyautogui.click()

# Print the time taken to execute the script
END = time.time()
print(f"Galaxy Flag Hack executed in {END - START:.2f} seconds")