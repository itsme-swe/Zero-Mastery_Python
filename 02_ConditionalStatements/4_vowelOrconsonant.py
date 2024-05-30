# Check if a given lower case character is a vowel or consonant

ch = input('Enter the lower case letter: ')

print('Vowel') if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' else print('Consonant')

print()

#◽ optimized solution by using Membership operator (in,  not in)

letter = input('Enter the lower case letter: ')

vowels = {'a', 'e', 'i', 'o', 'u'}

print('Vowel') if letter in vowels else print('Consonant')


