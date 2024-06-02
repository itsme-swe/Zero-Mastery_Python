#◽ Here we are using "index() method" to search an index value of particular element but it only return the first occurence of element

newList = [3, 6, 9, 11, 3, 13, 6, 9, 3]

print(newList.index(9))     # Output: 2 is indexValue of 9

print()

#◽Now we use "count() method" to know how many times the element occur in the list

print(newList.count(6))     # Output: 6 occurs 2 times in the list

print(newList.count(3))     # Output: 3 occurs 3 times in the list