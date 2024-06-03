# ◽ Method-1 To create set

s1 = {1, 2, 3, 4, 'jack', 3.4, 'jack'}

print(s1)   # Output: {'jack', 1, 2, 3, 4, 3.4} -- The output is in unordered form and did not allow duplicate values "jack" is printed only one time

print(type(s1))     # Output: <class 'set'> 

print()

# ◽ Method-2 To create set using set() object

s2 = set((1, 2, 'Harsh', 3+5j, 5.5))

print(s2)   # Output: {1, 'Harsh', 2, 5.5, (3+5j)}


