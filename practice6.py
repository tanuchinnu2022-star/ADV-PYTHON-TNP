t = (5, 15, "hi", 8, 20)

lst = list(t)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]

new_tuple = tuple(lst)
print("Updated tuple:", new_tuple)