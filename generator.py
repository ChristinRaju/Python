# A generator is a special type of function that automatically creates an iterator using the yield keyword.

# yield is like return, but it pauses the function, saving its state.

# You can resume from where it left off.


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration
