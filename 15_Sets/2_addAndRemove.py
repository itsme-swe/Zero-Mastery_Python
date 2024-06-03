# ◽Methods used to add and remove the elements from set

s1 = {5, 1, 3, 'Alice', 69.5, 50+2j}

print(s1)   # Output: {1, 3, 5, 69.5, (50+2j), 'Alice'}

s1.add('Harsh')     #🔸set.add() use to add the element in set

print(s1)   # Output: {1, 'Alice', 3, 'Harsh', 5, 69.5, (50+2j)}

s1.discard(50+2j)   #🔸set.discard() use to remove the element from list

print(s1)   # Output: {1, 3, 'Harsh', 5, 69.5, 'Alice'}