#◽+ concation operator used to join two list

list1 = [1, 2, 3, 4, 5, 6]

list2 = [7, 8, 9, 10]

list3 = list1 + list2

print(list3)

print()

list1.extend(list2)     # list.extend() method helps to modify the original list this is the another way to concatinate the list.

print(list1)    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]