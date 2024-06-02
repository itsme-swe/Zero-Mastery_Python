#◽Calculate Salary on the weekly basis given in a list

# Here we are using list comprehension and converting string into integer.
work_hrs = [int(x) for x in input("Enter hrs per day in entier week, seprated by space: ").split()]

wage = int(input('Enter the wages per hour: '))

total_workHours = sum(work_hrs)

print(f"The salary of whole week is \N{dollar sign}{total_workHours * wage}")

'''
🔸Output:
Enter hrs per day in entier week, seprated by space: 10 10 10 10 10 
Enter the wages per hour: 70
The salary of whole week is $3500
''' 