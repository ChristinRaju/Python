# An iterator is an object that allows you to loop through a sequence, one item at a time.

# To be an iterator, an object must implement two methods:

# __iter__() – returns the iterator object itself.

# __next__() – returns the next item or raises StopIteration when done.




# List is an iterable
nums = [10, 20, 30]

# Convert to iterator
it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # This will raise StopIteration
