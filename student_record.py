# Get student information
name = input("Enter your name: ")
regono = int(input("Enter your regno: "))
marks1 = int(input("Enter your marks1: "))
marks2 = int(input("Enter your marks2: "))
marks3 = int(input("Enter your marks3: "))

# Calculate total and average
total = marks1 + marks2 + marks3
avg = round(total / 3, 2)

# Grading logic
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"


passed = avg >= 40

# Printing the results
print(f"\nAverage: {avg:.2f}")
print(f"Grade: {grade}")
print(f"Passed: {passed}")

# Printing student record in a readable format
print("\nStudent Record:")
print(f"Name    : {name}")
print(f"Reg No  : {regono}")
print(f"Marks 1 : {marks1}")
print(f"Marks 2 : {marks2}")
print(f"Marks 3 : {marks3}")
print(f"Total   : {total}")
print(f"Average : {avg:.2f}")
print(f"Grade   : {grade}")
print(f"Passed  : {passed}")
