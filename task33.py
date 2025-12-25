list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

umumiy = []

for i in list1:
    if i in list2 and i not in umumiy:
        umumiy.append(i)

print(umumiy)
