#◽Checking and removing, if there is any duplicate value in list

l1 = [3, 5, 9, 8, 3, 4, 5, 9, 6, 3]

l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

l2.sort()   # sorting list in asceding form

print('List without duplicate values and in sorted form:', l2)

# Output: List without duplicate values and in sorted form: [3, 4, 5, 6, 8, 9]


'''
🔸We can remove duplicate values from list without creating new list with the help of set()
'''