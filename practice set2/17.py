s = input("Enter a string: ")

freq = {}

# Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")