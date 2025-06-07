class User:
    """Class to store user information and display it."""
    
    def __init__(self, first_name, last_name, dob, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.age = age
        self.location = location
        
    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUser Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"DOB: {self.dob}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}")
     
    def greet_user(self):
        """Prints a personalized greeting."""
        print(f"\nHello {self.first_name}, nice to see you again!")

# Function to force user input
def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:  # Ensures input is not empty
            return value
        print("This field cannot be empty. Please enter a value.")

# Collect user details
print("Enter user details:")

f_name = get_input("First name: ")
l_name = get_input("Last name: ")
dob = get_input("Date of birth: ")
age = get_input("Age: ")
location = get_input("Location: ")

# Create an instance of the User class
user_instance = User(f_name, l_name, dob, age, location)

# Call methods to greet and describe user
user_instance.greet_user()
user_instance.describe_user()