#◽Index Operator []

list1 = [1, 3, 5, 7, 9, 11, 13, 15]

list1[1] = 2    # writing

x = list1[1]    # reading

print(list1)    # Output: [1, 2, 5, 7, 9]

print(x)        # Output: 2

print()

#◽Slice Operator [ : ]
print(list1[:])     # Output: [1, 2, 5, 7, 9] --- if we pass only colon inside the square bracets[] it will print the entier list.

print(list1[2:])    # Output: [5, 7, 9] --- Now here this will start from index 2 till last of the list

list1[4:8] = [12, 14, 16, 18]

print(list1)    # Output: [1, 2, 5, 7, 12, 14, 16, 18] ---- We can modify the list with the help of slie operator just pass the startIndex and endIndex

# Syntax -- list[startIndex, endIdex, step]