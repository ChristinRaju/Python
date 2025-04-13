# 1. Single Inheritance 
# -> In single inheritance, a child class inherits the properties and methods of a single parent class.
 
class Animal: #Parent class
    def speak(self):
        return "Some sound"

class Dog(Animal): #Child class
    def speak(self):  
        return "Bark!"
    
dog = Dog()

print(dog.speak()) # Output: Bark!


# 2. Multiple Inheritance
# -> In multiple inheritance, a child class inherits the properties and methods of multiple parent classes.

class Engine:
    def Start(self):
        print("Engine started") 

class Wheels:
    def rotate(self):
        print("Wheels are rotating")

class Car(Engine, Wheels):  # Child class
    def drive(self):
        print("Car is driving")

# Create an object of Car
c = Car()

# Call methods directly, no need to wrap them in print()
c.Start()      # Output: Engine started
c.rotate()     # Output: Wheels are rotating
c.drive()      # Output: Car is driving


# 3. Multilevel Inheritance
# -> In multilevel inheritance, a child class inherits from a parent class, and then another child class inherits from that child class.

class Animal:
    def eat(self):
        print("Animal eats food.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Labrador(Dog):
    def weep(self):
        print("Labrador puppy weeps.")  # Match class name

# Object of the lowest class
puppy1 = Labrador()

# Calling all inherited and own methods
puppy1.eat()    # From Animal
puppy1.bark()   # From Dog
puppy1.weep()   # From Labrador


# 4. Hierarchical Inheritance
# -> In hierarchical inheritance, multiple child classes inherit from a single parent class.

class Animal:
    def eat(self):
        print("Animal eats food.")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks.")

class Cat(Animal):  # Cat also inherits from Animal
    def meow(self):
        print("Cat meows.")

# Create Dog object
dog1 = Dog()
dog1.eat()   # From Animal
dog1.bark()  # From Dog

# Create Cat object
cat1 = Cat()
cat1.eat()   # From Animal
cat1.meow()  # From Cat


# 5. Hybrid Inheritance
# -> In hybrid inheritance, a child class inherits from more than one parent class.