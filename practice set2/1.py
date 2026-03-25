import re

# Input list
lst = [10, 25, 3, 99, 56]

# Convert list to string
data = " ".join(map(str, lst))

# Use regex to extract numbers
numbers = re.findall(r'\d+', data)

# Convert to integers
numbers = list(map(int, numbers))

# Find largest element
largest = max(numbers)

print("Largest element:", largest)