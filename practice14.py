def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

b = int(input("Base: "))
e = int(input("Exponent: "))
print("Result:", power(b, e))