# Create a set to store registered emails
registered_emails = set()

def register_user():
    email = input("Enter your email to register: ").strip().lower() 
    if email in registered_emails:
        print(f"Error: {email} is already registered.")
    else:
        registered_emails.add(email)
        print(f"Success: {email} has been registered.")

while True:
    register_user()
    choice = input("Do you want to register another email? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Registration closed.")
        break
