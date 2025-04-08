# Global variable
visitor_count = 0

def new_visitor():
    global visitor_count
    visitor_count += 1
    print(f"Visitor number: {visitor_count}")

# Simulate multiple visitors
new_visitor()
new_visitor()
new_visitor()
print()

# Final visitor count
print(f"Total visitors so far: {visitor_count}")
