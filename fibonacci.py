n = int(input("Enter the number of Fibonacci numbers to print: "))

a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    next_value = a + b  # Calculate next number
    a = b  # Shift 'b' to 'a'
    b = next_value  # Update 'b' with the new value
