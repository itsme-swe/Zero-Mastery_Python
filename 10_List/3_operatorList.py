#◽+ Concation operator used to join two list

list1 = [1, 2, 3, 4, 5, 6]

list2 = [7, 8, 9, 10]

list3 = list1 + list2

print(list3)

print()

list1.extend(list2)     # list.extend() method helps to modify the original list this is the another way to concatinate the list.

print(list1)    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()

#◽Now we'll be using "in" and "not in" operator

print("Found") if 8 in list1 else print("Not Found")    # Output: Found --- Mostly we used "in" and "not in" operator with conditional statements.

print(15 not in list1)      # Output: True