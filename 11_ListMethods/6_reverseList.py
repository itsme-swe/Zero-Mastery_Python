#◽ Method used to reverse the list

list1 = [10, 15, 20, 25, 30, 35]

list1.reverse()

print(list1)    # Output: [35, 30, 25, 20, 15, 10]

print()

# Now to sort the list we use sort() method

l1 = [5, 1, 3, 2, 6, 8, 7, 9]

l1.sort()

print('List in ascending order:',l1)   # Output: List in ascending order: [1, 2, 3, 5, 6, 7, 8, 9] -- list is sorted in ascending order, this is by default when we use sort() method

print()

l2 = [20, 15, 12, 25, 22, 30, 28]

l2.sort(reverse = True)

print("List in descending order:",l2)   # Output: List in descending order: [30, 28, 25, 22, 20, 15, 12] -- to print list in descending order we need to pass "reverse = True" as parameter inside sort() method
