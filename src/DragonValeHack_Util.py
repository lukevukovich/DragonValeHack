# Item mapping for item and their Q-Word values
ITEM_MAPPING = {
    "galaxy flag": 2191473,
    "famed flat rock": 1500,
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
    print("")
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
    print("")
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
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_resources() -> dict:
    """
    Get multiple resources and their values from the user.
    """
    print("")
    resource_mapping = {}
    for resource, skips in RESOURCE_MAPPING.items():
        while True:
            try:
                value = input(f"Enter desired amount of {resource} (enter to skip): ").strip()
                if value == "":
                    break
                value = int(value)
                if value <= 0:
                    print("Please enter a positive value.")
                    continue
                if value > 0:
                    resource_mapping[resource] = {"value": value, "skips": skips}
                break
            except ValueError:
                print(f"Invalid input. Please enter a number for {resource}.")

    return resource_mapping


def get_add_or_remove() -> str:
    """
    Get whether to add or remove resources from the user.

    Returns:
        str: "add" or "remove" based on user input.
    """
    print("\n1. Add\n2. Remove")
    while True:
        try:
            choice = int(input("Select an option (1-2): ").strip())
            if choice == 1:
                return "add"
            elif choice == 2:
                return "remove"
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_num_entries() -> int:
    """
    Get the number of entries present from the user.

    Returns:
        int: The number of entries present.
    """
    print("")
    while True:
        try:
            num_entries = int(input("Enter the number of entries present: ").strip())
            if num_entries < 0:
                print("Please enter a non-negative number.")
                continue
            return num_entries
        except ValueError:
            print("Invalid input. Please enter a number.")