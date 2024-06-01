# Inserting elements to the list

l1 = [5, 10, 15, 20, 25, 30]

l1.append(35)

print(l1)   # [5, 10, 15, 20, 25, 30, 35]  By using append() method we can add value in the last of list

print()

#◽extend() Method is used to add collection

l1.extend([40, 45, 50])

print(l1)   # output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

'''
🔸 The main difference between "append()" and "extend()" is append() only add 1 value to list and extend() can add multiple values. 
'''

