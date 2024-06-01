#◽insert() method used to add element at given index value

l1 = [2, 4, 6 , 8, 10]

l1.insert(1, 3)

print(l1)   # output: [2, 3, 4, 6, 8, 10]

#🔸Syntax -- list.insert(indexVal, element)

print()

l2 = l1.copy()      # "copy()" method creates shallow list means it give us new list  

print("l2: ",l2)    # Output: l2:  [2, 3, 4, 6, 8, 10]