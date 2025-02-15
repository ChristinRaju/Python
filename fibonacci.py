n = int(input("Enter the number of Fibonacci numbers to print: "))

a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b 

