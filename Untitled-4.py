
marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]

# Remove marks below 40
valid = [m for m in marks if m >= 40]

# Remove duplicates and sort in ascending order
processed = sorted(set(valid))

# Select marks greater than or equal to 60
qualified = [m for m in processed if m >= 60]

# Find the top three marks in descending order
top_three = sorted(qualified, reverse=True)[:3]

print("Processed marks:", processed)
print("Qualified marks:", qualified)
print("Top three:", top_three)
