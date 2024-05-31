profile = "fullstack developer"

print(profile.find('full'))     # Output: 0 is the index value

print(profile.find('deve'))     # Output: 10 is the index value

print(profile.find('back'))     # # Output: -1 

'''
🔸find() method finds the first occurrence of the specified value.
   And, the find() method returns -1 if the value is not found.

   Syntax: string.find(valToBeSearched, startIndex, endIndex)   start and end Index are optional parameter
   
'''