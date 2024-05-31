# By using while loop print the table

n = int(input('Enter the number: '))
count = 1

while count <= 10:
    print(n, '*', count, '=', n * count)
    count += 1

''' ◽Output
    Enter the number: 5
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    5 * 10 = 50
'''