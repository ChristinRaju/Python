import random

print(random.uniform(5, 9))  # Generates a random float between 5 and 9
print(random.randint(1, 10))  # Generates a random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # Randomly selects an element from the list



list = [1, 2, 3, 4, 5]
print(random.shuffle(list))  # Shuffles the list in place
print(list)  # Prints the shuffled list
