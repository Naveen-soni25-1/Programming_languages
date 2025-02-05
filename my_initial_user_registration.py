# Lists to store usernames and passwords
usernames = ["naveen"]
passwords = ["12345678"]

while True:
    user_input_1 = input("Choose a username: ").strip().lower()

    # Check if username already exists
    if user_input_1 in usernames:
        print("Username already taken, try another.")
        continue  # Restart the loop to ask again

    # If username is unique, add it to the list
    usernames.append(user_input_1)

    # Get password input
    user_input_2 = input("Set password (minimum 8 characters): ").strip()

    # Validate password length
    if len(user_input_2) < 8:
        print("Password must be at least 8 characters long.")
        continue  # Restart the loop to ask again

    # Add password to the list
    passwords.append(user_input_2)

    print("User registered successfully!")
    
    # Show all registered usernames (for debugging)
    print(f"Registered usernames: {usernames}")

    break  # Exit loop after successful registration