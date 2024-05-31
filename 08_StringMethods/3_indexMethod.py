lang = "Python and Javascript"

print(lang.index('hon'))    # output: 3 is index value

print(lang.index('ru'))
''' Output
Traceback (most recent call last):
  File "E:\Zero-Mastery Python\08_StringMethods\3_indexMethod.py", line 5, in <module>
    print(lang.index('ru'))
          ^^^^^^^^^^^^^^^^
ValueError: substring not found
''' 

'''
🔸index() method finds the first occurrence of the specified value but index() method raises an exception if the value is not found and the find() method return -1.
  Syntax for index() and find() method is same.  
'''