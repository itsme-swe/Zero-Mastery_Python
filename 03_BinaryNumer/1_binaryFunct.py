# Function used to convert integer number into binary number 

a = 10

print(format(a, 'b'))   # format(a, 'b') a represent variable name and 'b' stands for binary

print(bin(a))   # output : 0b1010  ---- This is the another way to convert number into binary form

print(a.bit_length())       # Output: 4 "bit_length()" function used to see the length of binary number