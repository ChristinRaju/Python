def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ").lower()  
reversed_string = string[::-1]  

print(f"Reversed string: {reversed_string}")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


