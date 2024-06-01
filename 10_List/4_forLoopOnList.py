#◽Iterating over list using for Loop

list1 = [10, 20, 30, 40, 50]

for x in list1:
    print(x, end = ' ')         # Output: 10 20 30 40 50 

print()

for i in range(len(list1)):
    print(list1[i], end = ' ')  # Output: 10 20 30 40 50

print()

#◽Now printing list in reverse order

for i in range(len(list1)-1, -1, -1):
    print(list1[i], end=' ')     # Output: 50 40 30 20 10 