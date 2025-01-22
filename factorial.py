num = int(input("Enter an integer number: "))

# Initialize the factorial variable to 1
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")
