# 1. If Statement
print("\n=== Simple If Statement ===")
age = 18
if age >= 18:
    print("You are an adult")

# 2. If-else Statement
print("\n=== If-else Statement ===")
number = 15
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. elif Statement
print("\n=== elif Statement ===")
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

# 4. Short Hand If
print("\n=== Short Hand If ===")
age = 20
print("Can vote") if age >= 18 else print("Cannot vote")

# 5. While Loop
print("\n=== While Loop ===")
count = 0
while count < 3:
    print(count)
    count += 1

# 6. For Loop with Range
print("\n=== For Loop with Range ===")
for i in range(3):
    print(i)

# 7. Nested Loop
print("\n=== Nested Loop ===")
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# 8. Break Statement
print("\n=== Break Statement ===")
for i in range(5):
    if i == 3:
        break
    print(i)

# 9. Continue Statement
print("\n=== Continue Statement ===")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 10. While-else Statement
print("\n=== While-else Statement ===")
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed")

# 11. For-else Statement
print("\n=== For-else Statement ===")
for i in range(3):
    print(i)
else:
    print("For loop completed") 