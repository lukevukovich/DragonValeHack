# Item mapping for item and their Q-Word values
ITEM_MAPPING = {
    "galaxy flag": 2191473,
    "mini moss rock": 750,
}

# Resource mapping for resource and number of data entries to skip
RESOURCE_MAPPING = {
    "DragonCash": 0,
    "EXP": 2,
    "Food": 4,
    "Gems": 6,
    "Event Currency": 10,
    "Wishes": 12,
    "Eternal essence": 16,
    "Abundant essence": 18,
    "Vital essence": 20,
    "Ethereum": 22
}


def get_item() -> str:
    """
    Get the item to hack from the user.

    Returns:
        str: The selected item.
    """
    for i, item in enumerate(ITEM_MAPPING.keys()):
        print(f"{i + 1}. {item.title()}")

    while True:
        try:
            choice = int(input(f"Select the item to hack (1-{len(ITEM_MAPPING)}): ").strip()) - 1
            if 0 <= choice < len(ITEM_MAPPING):
                choice_str = list(ITEM_MAPPING.keys())[choice]
                return choice_str
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(ITEM_MAPPING)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_resource() -> str:
    """
    Get the resource to hack from the user.

    Returns:
        str: The selected resource.
    """
    for i, resource in enumerate(RESOURCE_MAPPING.keys()):
        print(f"{i + 1}. {resource}")

    while True:
        try:
            choice = int(input(f"Select the resource to hack (1-{len(RESOURCE_MAPPING)}): ").strip()) - 1
            if 0 <= choice < len(RESOURCE_MAPPING):
                choice_str = list(RESOURCE_MAPPING.keys())[choice]
                return choice_str
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(RESOURCE_MAPPING)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_resource_value(resource: str) -> int:
    """
    Get the resource value to hack from the user.
    """
    while True:
        try:
            value = int(input(f"Enter desired amount of {resource}: ").strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_success_flag() -> bool:
    """
    Get the success flag from the user.

    Returns:
        bool: True if the hack was successful, False otherwise.
    """
    while True:
        try:
            choice = input("Was the hack successful? (y/n): ").strip().lower()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")
