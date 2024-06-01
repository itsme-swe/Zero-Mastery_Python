#◽Method 1 to create list
list1 = ['Harsh', 'Mukul', 'Python', 'JavaScript']

print(list1)    # Output: ['Harsh', 'Mukul', 'Python', 'JavaScript']
print(type(list1))  # Output: <class 'list'>

print()

#◽Method 2 to create list
list2 = list(('Volvo', 'BMW', 'Mercedes'))

print(list2)    # Output: ['Volvo', 'BMW', 'Mercedes']
print(type(list2))  # Output: <class 'list'>

print()

#◽ List is Hetrogenous means can store different type of datatypes inside it. And, list is mutable means can be modified
myList = ['Harsh', True, 'Mehra', 69.5, 5+7j]
print(myList)   # Output: ['Harsh', True, 'Mehra', 69.5, (5+7j)]