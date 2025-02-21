num = int(input("Enter a number: "))
n = num

factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(f"The factorial of {n} is {factorial}")
