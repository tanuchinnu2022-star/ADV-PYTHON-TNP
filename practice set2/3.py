s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev   # add each character in front

print("Reversed string:", rev)