lst = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst)   # handle large k
rotated = lst[-k:] + lst[:-k]

print("Rotated list:", rotated)