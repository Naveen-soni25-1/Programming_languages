from user_module import User, Admin

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

# Handle Admin User
if f_name.lower() == "admin":
    admin_user = Admin("Naveen", "Soni", "25/01/2006", 19, "Tokyo, Japan")
    admin_user.greet_user()
    admin_user.describe_user()
    admin_user.show_privileges()
else:
    # Collect remaining details only for regular users
    l_name = get_input("Last name: ")
    dob = get_input("Date of birth: ")
    age = get_input("Age: ")
    location = get_input("Location: ")
    
    try:
        # Create a User instance only if it's not admin
        user_instance = User(f_name, l_name, dob, age, location)
        user_instance.greet_user()
        user_instance.describe_user()
    except NameError as e:
        print(f"Error: {e}")
