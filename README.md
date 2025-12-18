# DragonValeHack
Python scripts built to automate DragonVale resource exploits using Nox emulator and GameGuardian.

## How It Works
DragonVale has no server-side checks for resources, so it is possible to manipulate the game client to give you any amount of resources you want.

GameGuardian enables dynamic memory scanning and editing within the emulator. This allows resource values like DragonCash or Gems to be intercepted and changed.

pyautogui simulates mouse movements, clicks, and keyboard inputs on the Nox emulator and GameGuardian window, allowing full automation of the hacking process.

---

## Requirements

### Software Requirements
- [Python](https://www.python.org/downloads/)
- [Nox Emulator](https://www.bignox.com/) with DragonVale installed
- [GameGuardian](https://gameguardian.net/forum/files/file/2-gameguardian/) ([Installation](https://www.youtube.com/watch?v=WkpWSa5AsLs))

### Python Requirements
- pyautogui
- pyperclip

Use `pip install pyautogui pyperclip` to install the required Python packages.

### Game Guardian Setup
Ensure DragonVale is running before starting GameGuardian as it causes DragonVale to crash otherwise.

Once GameGuardian is installed in Nox, start the app and choose DragonVale from the process list.
Then navigate to configurations, and choose `Select memory ranges`. Ensure `O: Other` is checked, can leave everything else default.

---

## Supported Resources
- DragonCash
- EXP
- Food
- Gems
- Event Currency
- Wishes (if user has wishing well)
- Eternal essence (if applicable)
- Abundant essence (if applicable)
- Vital essence (if applicable)
- Ethereum

---

## Toolkit

### Item Hack (ItemHack_Main.py)
Automates the process of hacking in an item for free from the market.
Process will intercept item's sell value and change it to 0.

This item will later be used to hack resources.

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
Can add or remove resources.

#### Usage
- Ensure GameGuardian is running and DragonVale is open
- Ensure item (Famed Flat Rock or Galaxy Flag) is selected and "Buy Another" option is present
- Run script
- Select resource to hack
- Enter amount to hack
- Select Add or Remove
- Select item using to hack (Famed Flat Rock or Galaxy Flag)

### Multi-Resource Hack (MultiResourceHack_Main.py)
Automates the process of hacking multiple resources with any value through one sale.
Process will intercept item's "Buy Another" value and alter the resources and values they return.
Can add or remove resources.

#### Usage
- Ensure GameGuardian is running and DragonVale is open
- Ensure item (Famed Flat Rock or Galaxy Flag) is selected and "Buy Another" option is present
- Run script
- Enter amount to hack for each resource
- Select Add or Remove
- Select item using to hack (Famed Flat Rock or Galaxy Flag)