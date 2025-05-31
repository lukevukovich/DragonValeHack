# DragonValeHack
Python scripts built to automate DragonVale exploits using GameGuardian and Nox emulator.

All processes support 1080p resolution (fullscreen windowed).

## Python Requirements
- pyautogui
- pyperclip

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

## Item Hack (ItemHack_Main.py)
Automates the process of hacking in an item for free from the market.
Process will intercept the item's sell value and change it to 0.

### Items
- Famed Flat Rock (under level 11)
- Galaxy Flag (level 11 and above)

---

## Resource Hack (ResourceHack_Main.py)
Automates the process of hacking a resource with any value.
Process will intercept an item's "Buy Another" value and alter the resource and the value it returns.
Can add or remove resources.

- User must enter number of entries found during item search in order to guarantee hack success.

## Multi Resource Hack (MultiResourceHack_Main.py)
Automates the process of hacking multiple resources with any value through one sale.
Process will intercept and item's "Buy Another" value and alter the resources and values they return.
Can add or remove resources.

- User must enter number of entries found during item search in order to guarantee hack success.