# Get input from user and convert to integer
num = int(input("Enter a number: "))

# Initialize variables
factorial = 1

# Calculate factorial using while loop
while num > 0:
    factorial *= num
    num -= 1

# Print the result
print("The factorial is", factorial)
