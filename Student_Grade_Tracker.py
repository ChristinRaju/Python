# Student Grade Tracker

students = {}  # Dictionary to store student data

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
    else:
        students[name] = []  # Initialize with empty grade list
        print(f"Student '{name}' added.")

def add_grade():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
        return
    
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            students[name].append(grade)
            print(f"Grade {grade} added for {name}.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def calculate_average(name):
    grades = students[name]
    if grades:
        return sum(grades) / len(grades)
    return 0.0

def view_student():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
        return
    
    grades = students[name]
    print(f"\nGrades for {name}: {grades}")
    
    avg = calculate_average(name)
    print(f"Average Grade: {avg:.2f}")
    
    passed = avg >= 50  # Boolean
    print("Status: " + ("✅ Passed" if passed else "❌ Failed"))

def view_all_students():
    if not students:
        print("No students added yet.")
        return
    
    for name in students:
        avg = calculate_average(name)
        status = "Passed" if avg >= 50 else "Failed"
        print(f"{name}: Grades={students[name]}, Average={avg:.2f}, Status={status}")

def menu():
    while True:
        print("\n===== Student Grade Tracker =====")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Info")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
menu()
