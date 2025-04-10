class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Woof!"
class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Meow!"
    
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
