def print_message(unsend, sended):
    """Print unsend messages and move them
    to the sended list"""
    print("Enter 'done' when finished:".title())

    temp_unsend = unsend[:]  # Create a copy of the original unsend list

    while temp_unsend:  # Process messages from the copied list
        current_message = temp_unsend.pop(0)
        print(f"Sending message: “{current_message}”".title())
        sended.append(current_message)

def show_message(sended):
    if sended:
        print("\nFollowing messages have been sent:")
        for message in sended:
            print(message)

# Original message list
unsend = ["Hello", "How are you?", "This is a test."]
sended = []

# Pass a copy of the unsend list to preserve the original
print_message(unsend[:], sended)
show_message(sended)

# Checking the original list remains unchanged
print("\nOriginal unsend list:", unsend)
