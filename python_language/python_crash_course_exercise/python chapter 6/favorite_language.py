# An Empty dictionary for people
favorite_language = {}

# Greetings to people 
print("Welcome to the poll")
print("To see the poll result, enter [show]")

while True:  # A loop till break
    name = input("\nWhat is your name: ").strip()

    if name.lower() == 'show':  # To see results
        print("\nHere's the poll result:")
        for i, key in enumerate(favorite_language, start=1):  # Start from 1
            print(f"{i}. {key}: {favorite_language[key]}")
        break

    elif name in favorite_language:  # If name already exists
        add = input("Do you want to add more (yes/no): ").strip().lower()
        if add == 'yes':
            inp = input("Enter it: ").strip()
            favorite_language[name].append(inp)
        
    else:  # New user
        ask = input("What is your favorite language: ").strip()
        favorite_language[name] = [ask]
