def square_numbers(nums):  # Defines a generator function
    for i in range(nums):  # Loops from 0 to nums-1
        yield i * i        # Yields the square of i
        
gen = square_numbers(6)     # Creates a generator for numbers 0 to 2
print(list(gen))            # Converts generator output to a list and prints it
