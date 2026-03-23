words = ["madam", "hello", "level", "world", "radar"]

# Sort by length
sorted_words = sorted(words, key=len)
print("Sorted:", sorted_words)

# Palindromes
pal = [w for w in words if w == w[::-1]]
print("Palindromes:", pal)

# Replace spaces
sentence = "hello world python"
new_list = [w.replace(" ", "-") for w in sentence.split()]
print("Hyphenated:", new_list)