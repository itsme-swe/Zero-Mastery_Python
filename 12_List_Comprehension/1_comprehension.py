#◽Adding elements inside an empty list

l1 = []

for x in range(1, 11):
    l1.append(x)

print(l1)   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()

#◽ Another way to add elements inside the empty list without using append() function

l2 = [x for x in range(1, 11)]

print(l2)   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
