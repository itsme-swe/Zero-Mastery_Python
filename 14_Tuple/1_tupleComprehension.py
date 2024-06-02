# ◽Tuple Comprehension means easiest way to create tuple objects

t1 = tuple((x for x in range(1,11)))

print(t1)   #Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print()

t2 = (*(x for x in range(1,11,2)),)

print(t2)   # Output: (1, 3, 5, 7, 9)