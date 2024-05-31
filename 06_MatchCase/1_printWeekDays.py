# Print the week days according to the input given by the user

date = int(input('Enter the date: '))

match date:
    case 1:
        print('Sunday')

    case 2:
        print('Monday')

    case 3:
        print('Tuesday')

    case 4:
        print('Wednesday')

    case 5: 
        print('Thursday')

    case 6: 
        print('Friday')
    
    case 5: 
        print('Saturday')

    case _:
        print('Holiday')