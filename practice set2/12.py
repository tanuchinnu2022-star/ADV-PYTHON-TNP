lst = [10, 20, 10, 30, 20, 10]

freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency:", freq)