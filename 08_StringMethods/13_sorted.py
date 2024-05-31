# Sorting letter of a string

name = "jsdghdgatelc"

sortForm = sorted(name)

print(sortForm)     # Output: ['a', 'c', 'd', 'd', 'e', 'g', 'g', 'h', 'j', 'l', 's', 't']

newSort = ''.join(sortForm)     # Output: acddegghjlst --- With the help of join() method we can convert list into string 

print(newSort)

'''
🔸 The sorted() function returns a sorted list of the specified iterable object.
'''