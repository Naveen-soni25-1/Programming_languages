class Car: # car class 
    """ a simple attempt to represent the car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} km on it.")

my_car = Car("tesla", "model s", 2024)
print(my_car.get_description())
my_car.read_odometer()
