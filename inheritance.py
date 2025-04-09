class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent constructor
        self.breed = breed

    def speak(self):
        return "Woof!"

# Create a Dog object
dog1 = Dog("Buddy", "Labrador")

print(dog1.name)       # Output: Buddy
print(dog1.breed)      # Output: Labrador
print(dog1.speak())    # Output: Woof!
