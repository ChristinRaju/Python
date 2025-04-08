# This is the class (blueprint for creating car objects)
class Car:
    def __init__(self, brand, model, year):  # Constructor method
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):  # Method to display car info
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# These are objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)  # Object 1
car2 = Car("Honda", "Civic", 2019)     # Object 2

# Calling the method using the objects
car1.display_info()
car2.display_info()
