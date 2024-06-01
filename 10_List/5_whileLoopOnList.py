#◽Now we'll be using while loop to iterate over list

list1 = [2, 4, 6, 8, 10]

i = 0
while i < len(list1):
    print(list1[i], end=' ')
    i += 1

# Output: 2 4 6 8 10

print()

#◽ Reversing the list using while loop

i = len(list1) - 1

while i >= 0:
    print(list1[i], end=' ')
    i -= 1

# Output: 10 8 6 4 2