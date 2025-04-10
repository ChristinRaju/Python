# Get student information
student = {}
student["name"] = input("Enter your name: ")
student["regno"] = int(input("Enter your regno: "))

marks1 = int(input("Enter your marks1: "))
marks2 = int(input("Enter your marks2: "))
marks3 = int(input("Enter your marks3: "))

student["marks"] = [marks1, marks2, marks3]

# Calculate total and average
student["total"] = sum(student["marks"])
#student["avg"] = round(student["total"] / 3, 2)
student["avg"] = round(student["total"] / len(student["marks"]), 2)

# Grading logic
if student["avg"] >= 90:
    student["grade"] = "A"
elif student["avg"] >= 80:
    student["grade"] = "B"
elif student["avg"] >= 70:
    student["grade"] = "C"
elif student["avg"] >= 60:
    student["grade"] = "D"
else:
    student["grade"] = "F"

student["passed"] = student["avg"] >= 40


# Printing the results
print("\n========= Student Record =========")
print(f"Name    : {student['name']}")
print(f"Reg No  : {student['regno']}")
print(f"Marks   : {student['marks']}")
print(f"Total   : {student['total']}")
print(f"Average : {student['avg']:.2f}")
print(f"Grade   : {student['grade']}")
print(f"Passed  : {student['passed']}")