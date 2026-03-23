students = {}

# Add
students["A"] = {"marks": [80, 90, 85]}
students["B"] = {"marks": [70, 75, 65]}

# Update
students["A"]["marks"].append(95)

# Average
for name, data in students.items():
    avg = sum(data["marks"]) / len(data["marks"])
    print(name, "Average:", avg)

# Topper
topper = max(students, key=lambda x: sum(students[x]["marks"]))
print("Topper:", topper)