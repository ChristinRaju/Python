# A school wants to generate roll numbers for students automatically. Implement  
# a Python script that assigns unique roll numbers to students in a list.

students = ["Elias", "Paul", "Anna", "Hannah"]
students.sort()  # Sort students alphabetically

roll_prefix = "NU24UCA"
for i, student in enumerate(students):
    roll_number = f"{roll_prefix}{i + 1:03d}"
    print(f"{student} - Roll No: {roll_number}")
