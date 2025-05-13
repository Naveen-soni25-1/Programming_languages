toppings = []

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

print("Toppings added:", toppings)
