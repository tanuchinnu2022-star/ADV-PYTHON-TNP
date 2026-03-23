t = (1, "hi", 3.5, 7, "hello", 10)

# Filter numbers
nums = tuple(x for x in t if isinstance(x, (int, float)))
print("Numeric values:", nums)

# Attempt modification
try:
    t[0] = 100
except TypeError:
    print("Tuple cannot be modified")

# Concatenate
t2 = ("new", 99)
print("Concatenated tuple:", t + t2)