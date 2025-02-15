# 1. Lists - Mutable, ordered collection
print("\n=== Lists ===")
fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)
fruits.append("grape")              # Add item
fruits[0] = "pear"                 # Modify item
fruits.remove("banana")            # Remove item
print("Modified list:", fruits)
print("First fruit:", fruits[0])   # Access by index

# 2. Tuples - Immutable, ordered collection
print("\n=== Tuples ===")
coordinates = (10, 20)
print("Coordinates:", coordinates)
x, y = coordinates                 # Tuple unpacking
print(f"X: {x}, Y: {y}")

# 3. Strings - Immutable sequence of characters
print("\n=== Strings ===")
text = "Hello, World!"
print("Original:", text)
print("Uppercase:", text.upper())
print("Length:", len(text))
print("Slice:", text[0:5])        # String slicing

# 4. Sets - Unordered collection of unique elements
print("\n=== Sets ===")
numbers = {1, 2, 3, 2, 4, 3, 5}   # Duplicates are removed
print("Set:", numbers)
numbers.add(6)                     # Add item
numbers.remove(1)                  # Remove item
print("Modified set:", numbers)

# 5. Dictionaries - Key-value pairs
print("\n=== Dictionaries ===")
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 88]
}
print("Original dict:", student)
student["age"] = 21               # Modify value
student["city"] = "New York"      # Add new key-value
print("Modified dict:", student)
print("Name:", student["name"])   # Access by key

# 6. Common Operations
print("\n=== Common Operations ===")

# List operations
numbers_list = [1, 2, 3, 4, 5]
print("List sum:", sum(numbers_list))
print("List max:", max(numbers_list))
print("List sorting:", sorted(numbers_list, reverse=True))

# String operations
message = "python programming"
print("Capitalized:", message.capitalize())
print("Contains 'prog':", "prog" in message)
print("Replace:", message.replace("python", "Python"))

# Dictionary operations
for key, value in student.items():
    print(f"{key}: {value}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2) 