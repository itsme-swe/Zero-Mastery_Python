# Check if the number is palindrome 

n = int(input('Enter the number: '))

m = n       # Storing original number into another variable

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

print('Number is palindrome') if m == rev else print('Not an palindrome')