def add_guest(guest_list, guest_name):
    """
    Function to add a guest to the guest list.

    Args:
    guest_list (set): The current set of guests.
    guest_name (str): The name of the guest to add.

    Returns:
    None
    """
    pass


def remove_duplicate_guests(guest_list_with_duplicates):
    """
    Function to remove duplicate guests from a guest list using a set.

    Args:
    guest_list_with_duplicates (list): A list of guest names that may contain duplicates.

    Returns:
    set: A set of unique guest names.
    """
    pass


def remove_guest(guest_list, guest_name):
    """
    Function to remove a guest from the guest list.

    Args:
    guest_list (set): The current set of guests.
    guest_name (str): The name of the guest to remove.

    Returns:
    None
    """
    pass


def clear_guest_list(guest_list):
    """
    Function to clear the entire guest list.

    Args:
    guest_list (set): The current set of guests.

    Returns:
    None
    """
    pass


# Example usage:

# Initial guest list with duplicates
guest_list_with_duplicates = ["Alice", "Bob", "Charlie",
                              "Alice", "David", "Eve", "Bob", "Charlie", "Eve", "Frank"]

# Remove duplicates by converting to a set
guest_list = remove_duplicate_guests(guest_list_with_duplicates)

# Add new guests
add_guest(guest_list, "Grace")
add_guest(guest_list, "Hank")

# Remove a guest
remove_guest(guest_list, "Alice")

# Clear the guest list
clear_guest_list(guest_list)

# Check the final state of the guest list
print("Final guest list:", guest_list)
