rollNo = 101
name = 'Ravi'
avg = 86.50

print("Student name is %s, his roll number is %d and average is avg %f"%(name, rollNo, avg))

''' 🔸Output:
Student name is Ravi, his roll number is 101 and average is avg 86.500000. 

Python supports C language string formatting too.
◽ "%f" stands for float value.
◽ "%d" stands for decimal value.
◽ "%s" stands for string value.
◽ "%i" stands for integer value.
◽ "%o" stands for octal value.
◽ "%x" stands for hexa decimal value.
'''

print("Student roll number is %5d"%rollNo)      # Output: Student roll number is   101 --- This will add 5 spaces b/w the sentence and roll number