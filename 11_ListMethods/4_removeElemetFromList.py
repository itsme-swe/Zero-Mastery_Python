#◽Here we are using another methods to remove the items from list
list1 = [5, 6, 21, 5, 10, 6, 20]

list1.remove(5)

print(list1)    # Output: [6, 21, 5, 10, 6, 20] -- The element 5 has been removed from list present at index val 0 and this was the first occurence of 5

print()

list1.clear()

print(list1)    # Output: [] Empty List

print()

l1 = [1, 2, 3, 4, 5, 6]

del l1[:]

print(l1)   # Output: [] Empty list