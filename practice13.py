import string

s = input("Enter sentence: ")

# Remove spaces & punctuation
clean = "".join(ch for ch in s if ch.isalnum())

result = set()

for ch in clean:
    if clean.count(ch) == 1:
        result.add(ch)

print("Unique characters:", result)