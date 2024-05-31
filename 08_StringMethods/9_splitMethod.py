msg = "Welcome to the jungle"

print(type(msg))    # Output: <class 'str'>

newMsg = msg.split()

print(msg)      # Output: Welcome to the jungle

print(newMsg)   #Output: ['Welcome', 'to', 'the', 'jungle']

print(type(newMsg))     # Output: <class 'list'>

'''
🔸split() method splits a string into a list.

   Syntax:  string.split(separator, maxsplit) Both the parameters are optional
'''