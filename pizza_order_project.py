print("Hello customer,\nwelcome to PizzaHub".title())

print("\nWhen done with toppings or if you don't need any, enter [done].".title())

menu = "\nmenu:\n'mushroom', 'olives', 'green peppers', 'pineapple', 'extra cheese', 'pepperoni', 'tomato'"
print(menu.title())

# List of available toppings
available_toppings = ['mushroom', 'olives', 'green peppers', 'pineapple', 'extra cheese', 'pepperoni', 'tomato']

# List to store user-selected toppings
requested_toppings = []

# Loop to take user input
while True:
    user = input("\nWhat topping would you like? ".title()).strip().lower()

    # Exit the loop when user is done
    if user == 'done':
        if requested_toppings:
            print("\nYour pizza is ready with the following toppings🥘:".title())
            for topping in requested_toppings:
                print(f"- {topping.title()}")
            break  # Exit the loop after displaying toppings
        else:  # Handle the case where the user enters 'done' with no toppings
            ask = input("\nAre you sure you need a plain pizza? (yes / no): ").strip().lower()
            if ask == 'yes':
                print("\nYour plain pizza is ready.".title())
                break
            else:
                continue # Go back to topping selection if no plain pizza

    elif user in available_toppings: #Use elif to prevent the "sorry we don't have" message when user types done
        requested_toppings.append(user)
        print(f"{user.title()} added to your pizza.")

    else:  # Corrected logic: only print "we don't have" if the topping is truly invalid
        print(f"Sorry, we don't have {user}.")
