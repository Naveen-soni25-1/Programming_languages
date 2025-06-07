# Stores guest names in a file
filename = 'guest_book.txt'

while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == 'q':
        break
    with open(filename, 'a') as file: # open the file in append mode
        # a mean append and use for adding new contents to the file.
        file.write(f"{name}\n")
    print(f"Welcome, {name}!")
