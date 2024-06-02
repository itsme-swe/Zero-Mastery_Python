#◽Now methods to remove elements from List:

lst1 = [10, 5, 12, 4, 20, 25, 30]

lst1.pop()

print(lst1)     # Output: [10, 5, 12, 4, 20, 25] -- this is the list after using pop() method without passing index value

lst1.pop(3)

print(lst1)     # Output: [10, 5, 12, 20, 25] -- this is the list after passing the index value(3). The element present at index value 3 is removed

del lst1[0]

print(lst1)     # Output: [5, 12, 20, 25] -- This del listName[indexVal] function work same as pop() method to remoe the element from list 


