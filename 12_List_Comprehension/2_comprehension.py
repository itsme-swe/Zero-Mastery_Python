#◽ Now here adding those elements from tuple in list which are divisible by 2 

l1 = [x for x in (2, 6, 9, 11, 12, 15, 18) if x % 2 == 0]

print(l1)   # Output: [2, 6, 12, 18]