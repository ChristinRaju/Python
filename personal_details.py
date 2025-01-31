def personal_details(name, age, is_student):
    print("Name:", name)
    print("Age:", age)
    print("Is Student:", is_student)
    if is_student:
        print("You are a student")
    else:
        print("You are not a student")
        
    if age < 18:
        print("You are a minor")    
    elif age >= 18 and age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")
        
        
def main():
    print("This is the main function")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    is_student_input = input("Are you a student? (yes/no): ").lower() 
    is_student = is_student_input == "yes" 
    
    personal_details(name, age, is_student)

# duner name variable
if __name__ == "__main__": 
    main()
