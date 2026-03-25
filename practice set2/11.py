lst = [10, 20, 10, 30, 20, 40]
unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List without duplicates:", unique)