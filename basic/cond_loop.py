"""
    Program uses conditional statements and loops
    to complete a FizzBuzz statement.
    Rules:
        If the number is divisible by both 3 and 5: FizzBuzz
        Only by 3: Fizz
        Only by 5: Buzz
"""

# Ask the user to enter the number
print('Enter a number between 1 and 100: ')
number = int(input())

for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz', end=', ')
    elif i % 3 == 0:
        print('Fizz', end=', ')
    elif i % 5 == 0:
        print('Buzz', end=', ')
    


