domain = "backend"

x = domain.ljust(10)

y = domain.ljust(10, '*')

print(x, "development")     # Output: backend    development

print(y)    # Output: backend***

'''
🔸ljust() method will left align the string. This method returns a new string of a specified length with the original string left-aligned and padded with spaces (or an optional specified character) on the right side.

'''