# 1. Nested If Conditions
print("\n=== Nested If Conditions ===")
age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("You can enter the club")
    else:
        print("Sorry, you need ID")
else:
    print("Too young to enter")

# 2. Nested If-Elif-Else
print("\n=== Nested If-Elif-Else ===")
score = int(input("Enter your score: "))

if score >= 60:
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Grade F")

# 3. Break Statement Examples
print("\n=== Break Statement Examples ===")
# Break in while loop
print("While loop with break:")
counter = 0
while True:
    if counter == 5:
        break
    print(counter, end=" ")
    counter += 1

# Break in for loop
print("\nFor loop with break:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

# 4. Continue Statement Examples
print("\n\n=== Continue Statement Examples ===")
# Continue in while loop
print("While loop with continue:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")

# Continue in for loop
print("\nFor loop with continue:")
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")

# 5. Pass Statement Examples
print("\n\n=== Pass Statement Examples ===")
# Pass in if statement
number = 10
if number > 0:
    pass  # TODO: Add code later
else:
    print("Negative number")

# Pass in function
def my_function():
    pass  # Empty function

# Pass in class
class MyClass:
    pass  # Empty class

# 6. Complex Nested Example
print("\n=== Complex Nested Example ===")
for i in range(5):
    if i == 0:
        continue  # Skip first iteration
    elif i == 3:
        break    # Stop at 3
    else:
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd") 