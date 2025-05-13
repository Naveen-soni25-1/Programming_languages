number = float(input("Choose a number [1,2,3,4,5,6,7,8,9]: "))
operation = (number * 2)
add = (operation + 5)
yo = add*50

birthday = input("Have you had your birthday this year? (yes/no): ").lower()

if birthday.lower() == "yes":
    age_base = yo + 1775
else:
    age_base = yo + 1774

birth_date = int(input("What is your birth year? "))  # Convert to int

result = age_base - birth_date  # Calculate age
if birth_date > 2025 or birth_date < 1900:
    print("please put vailed birth year !")
else:
    print(result)  # Corrected print statement'