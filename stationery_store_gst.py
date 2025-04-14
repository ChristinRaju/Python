# Step 1: List of customer order amounts (before GST)
orders_total = [100, 250.50, 75, 180, 120.75]

# Step 2: Add 18% GST to each order using lambda and map
final_bills = list(map(lambda x: round(x * 1.18, 2), orders_total))

# Step 3: Print final bill for each customer
print("Final bills (including 18% GST):")
for i in range(len(final_bills)):
    print(f"Customer {i+1}: ₹{final_bills[i]}")
