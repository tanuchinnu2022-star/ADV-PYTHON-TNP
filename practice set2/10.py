lst = [10, 20, 5, 8, 20, 15]

unique_lst = list(set(lst))   # remove duplicates
unique_lst.sort()

print("Second largest:", unique_lst[-2])