# Stores poll responses in a file
filename = 'programming_poll.txt'

while True:
    reason = input("Why do you love programming? (q to quit): ")
    if reason == 'q':
        break
    with open(filename, 'a') as file:
        file.write(f"{reason}\n")
    print(f"Thank you for your responde!.")