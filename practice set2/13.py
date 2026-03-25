list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged = []
i = j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list)