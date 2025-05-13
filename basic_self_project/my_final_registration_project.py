# Store usernames and passwords in a dictionary
users = {"naveen": "12345678"}

while True:
    user_input_1 = input("Choose a username: ").strip().lower()

    if user_input_1 in users:
        print("Username already taken, try another.")
        continue  # Ask for a new username

    user_input_2 = input("Set a password (min 8 characters): ").strip()

    if len(user_input_2) < 8:
        print("Password must be at least 8 characters long.")
        continue  # Ask for a new password

    # Store valid credentials
    users[user_input_1] = user_input_2
    print("User registered successfully!")
    
    # Display all registered users (for debugging purposes)
    print("Registered users:", list(users.keys()))

    break  # Exit after successful registration