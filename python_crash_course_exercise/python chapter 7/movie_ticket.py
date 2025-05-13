while True: # infinite loop
    age = input("Enter your age (or 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
