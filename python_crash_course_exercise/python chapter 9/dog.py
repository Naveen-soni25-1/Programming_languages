class Dog: # a class definition for dog objects.
    """ a simle attempt to make a dog."""
    def __init__(self, name, age): # this is a constructor method.
        self.name = name
        self.age = age # sttributes of the class.

    def sit(self):
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('bruno', 3) # an instance of the dog class.
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
