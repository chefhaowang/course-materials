def add_guest(guest_list, guest_name):
    if guest_name in guest_list:
        print(f"{guest_name} is already on the guest list.")
    else:
        guest_list.add(guest_name)
        print(f"Added {guest_name} to the guest list.")


def remove_duplicate_guests(guest_list_with_duplicates):
    unique_guests = set(guest_list_with_duplicates)
    print(f"Removed duplicates. Unique guest list: {unique_guests}")
    return unique_guests


def remove_guest(guest_list, guest_name):
    if guest_name in guest_list:
        guest_list.remove(guest_name)
        print(f"Removed {guest_name} from the guest list.")
    else:
        print(f"{guest_name} is not in the guest list.")


def clear_guest_list(guest_list):
    guest_list.clear()
    print("Cleared the guest list.")


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
