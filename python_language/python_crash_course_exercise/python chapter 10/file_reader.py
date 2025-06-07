# Reads a file and prints its content
filename = 'sample.txt'

try: # handle the error cases.
    with open(filename) as file_object:
        contents = file_object.read()
        print(contents.strip())
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
