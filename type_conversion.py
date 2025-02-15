# 1. Implicit Type Conversion (Automatic)
print("\n=== Implicit Conversion ===")
num_int = 10
num_float = 3.14
sum_numbers = num_int + num_float    # int is converted to float automatically
print(f"Integer {num_int} + Float {num_float} = {sum_numbers}")
print(f"Result type: {type(sum_numbers)}")

# 2. Explicit Type Conversion (Casting)
print("\n=== Explicit Conversion ===")
# String to Integer
str_num = "100"
converted_int = int(str_num)
print(f"String to Integer: {str_num} -> {converted_int} ({type(converted_int)})")

# Integer to Float
num = 50
converted_float = float(num)
print(f"Integer to Float: {num} -> {converted_float} ({type(converted_float)})")

# Float to Integer
float_num = 3.99
converted_int = int(float_num)    # Truncates decimal part
print(f"Float to Integer: {float_num} -> {converted_int} ({type(converted_int)})")

# Number to String
num = 25
str_num = str(num)
print(f"Number to String: {num} -> {str_num} ({type(str_num)})")

# 3. String Operations and Conversion
print("\n=== String Operations ===")
# String concatenation
first_name = "John"
age = 25
message = first_name + " is " + str(age) + " years old"
print("Concatenation:", message)

# f-string (modern way)
message = f"{first_name} is {age} years old"
print("f-string:", message)

# String methods
text = "  Python Programming  "
print("Original:", text)
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())
print("Split:", text.split())

# 4. Type Conversion Examples
print("\n=== Practical Examples ===")
# User input conversion
user_input = input("Enter a number: ")
number = int(user_input)
doubled = number * 2
print(f"Doubled: {doubled}")

# List conversion
numbers = [1, 2, 3, 4, 5]
# Convert list to string
str_numbers = str(numbers)
print(f"List to string: {str_numbers} ({type(str_numbers)})")
# Convert list to tuple
tuple_numbers = tuple(numbers)
print(f"List to tuple: {tuple_numbers} ({type(tuple_numbers)})")
# Convert list to set
set_numbers = set(numbers)
print(f"List to set: {set_numbers} ({type(set_numbers)})") 