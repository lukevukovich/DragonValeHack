<p align="center">
  <img src="assets/gems.png" alt="DragonValeHack logo" width="64" />
</p>

<h1 align="center">DragonValeHack</h1>

<p align="center">Python scripts designed to automate DragonVale resource exploits using Nox emulator and GameGuardian.</p>

## How It Works
DragonVale has no server-side checks for resources, so it is possible to manipulate the game client to give you any amount of resources you want.

GameGuardian enables dynamic memory scanning and editing within the emulator. This allows resource values like DragonCash or Gems to be intercepted and changed.

pyautogui simulates mouse movements, clicks, and keyboard inputs on the Nox emulator and GameGuardian window, allowing full automation of the hacking process.

---

## Requirements & Setup

### Software Requirements
- [Python](https://www.python.org/downloads/)
- [Nox Emulator](https://www.bignox.com/) with DragonVale installed
- [GameGuardian](https://gameguardian.net/forum/files/file/2-gameguardian/) ([Installation](https://www.youtube.com/watch?v=WkpWSa5AsLs))

### Python Requirements
- Python 3.9 or higher
- pyautogui
- pyperclip

Use `pip install pyautogui pyperclip` to install the required Python packages.

### Nox Setup
- **Performance Settings:**
    - High (4 cores CPU, 4096 MB Memory)
    - Tablet mode
    - 1920x1080 resolution

- **Gaming Settings:**
    - Frame settings: >= 60 FPS

- **General Settings:**
    - Root: Enabled

Ensure Nox is in windowed mode and maximized in order for pyautogui to work correctly.

### Game Guardian Setup
Ensure DragonVale is running before starting GameGuardian as it causes DragonVale to crash otherwise.

Once GameGuardian is installed in Nox, start the app and choose DragonVale from the process list.
Then navigate to configurations, and choose `Select memory ranges`. Ensure `O: Other` is checked, can leave everything else default.

---

## Toolkit

### Common

#### DragonValeHack Class (src/DragonValeHack.py)
Contains common functions and constants used by all hack scripts.
Intended to be extensible and reusable for future hacks/updates.

#### DragonValeHack Utilities (src/DragonValeHack_Utils.py)
Contains utility functions for user input and validation.

### Item Hack (ItemHack_Main.py)
Automates the process of hacking in an item for free from the market.
Process will intercept item's sell value and change it to 0.

__Note:__ This item can later be used to hack resources. If you have enough money to buy items (e.g. Galaxy Flag), you can probably skip this hack.

#### Supported Items
- Famed Flat Rock (under level 11)
- Galaxy Flag (level 11 and above)

#### Usage
- Ensure GameGuardian is running and DragonVale is open
- Ensure screen is focused on a free 1x1 slot to place item
- Run script
- Select item to hack for free (Famed Flat Rock or Galaxy Flag)

### Resource Hack (ResourceHack_Main.py)
Automates the process of hacking a resource with any value.
Process will intercept item's "Buy Another" value and alter the resource and the value it returns.
Supports adding and removing resources.

#### Usage
- Ensure GameGuardian is running and DragonVale is open
- Ensure item (Famed Flat Rock or Galaxy Flag) is selected and "Buy Another" option is present (with free 1x1 slot nearby)
- Run script
- Select resource to hack
- Enter amount to hack
- Select Add or Remove
- Select item using to hack (Famed Flat Rock or Galaxy Flag)

### Multi-Resource Hack (MultiResourceHack_Main.py)
Automates the process of hacking multiple resources with any value through one sale.
Process will intercept item's "Buy Another" value and alter the resources and values they return.
Supports adding and removing resources.

#### Usage
- Ensure GameGuardian is running and DragonVale is open
- Ensure item (Famed Flat Rock or Galaxy Flag) is selected and "Buy Another" option is present (with free 1x1 slot nearby)
- Run script
- Enter amount to hack for each resource
- Select Add or Remove
- Select item using to hack (Famed Flat Rock or Galaxy Flag)

### Toolkit Notes
- If hacks are not working, ensure all setup and usage steps were followed correctly
- Feel free to change timing values in the scripts if your machine is slower/faster
- These hacks are fragile and may not work after game updates. Feel free to fork and modify as needed
- I over-commented the hacks to make maintenance easier and to help others learn follow along

---

## Supported Resources
The following resources can be hacked using this toolkit (availability may depend on user level and game progress):
- DragonCash
- EXP
- Food
- Gems
- Event Currency (if applicable)
- Wishes (if user has wishing well)
- Eternal essence (if applicable)
- Abundant essence (if applicable)
- Vital essence (if applicable)
- Ethereum

---

## Disclaimer
This project is intended for educational and research purposes only.
The author does not condone cheating, hacking, or violating the terms of service of any software, including DragonVale.
Use of these scripts may violate the terms of service of DragonVale and related software.
The author is not responsible for any misuse or consequences resulting from the use of this code.
By using this project, you agree to use it at your own risk and to comply with all applicable laws and terms of service.

---

<p align="center">
  <img src="assets/proof.png" alt="DragonValeHack proof image" />
</p>