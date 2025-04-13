#Write a python program to swap two numbers with and without using temp

print("\n========= Swapping with a temporary variable =========")
x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: ', x)
print('The value of y after swapping: ', y)

print("\n========= Swapping without a temporary variable =========")
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

x = x + y
y = x - y
x = x - y

print('The value of x after swapping: ', x)
print('The value of y after swapping: ', y)
