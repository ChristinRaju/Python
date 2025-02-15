n = int(input("Enter how many even numbers to print: "))
count = 0
number = 0

while count < n:
    if number % 2 == 0:
        print(number, end=" ")
        count += 1
    number += 1 