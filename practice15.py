s = input("Enter string: ")

# Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

vowels = "aeiouAEIOU"
v = c = d = sp = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special chars:", sp)