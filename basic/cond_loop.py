"""
    The first program uses conditional statements and loops
    to complete a FizzBuzz statement.
    Rules:
        If the number is divisible by both 3 and 5: FizzBuzz
        Only by 3: Fizz
        Only by 5: Buzz

    The second program finds the smallest or largest number
    in a set of numbers.
"""


def fizz_buzz():
    print('Enter a number between 1 and 100: ')
    number = int(input())

    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=', ')
        elif i % 3 == 0:
            print('Fizz', end=', ')
        elif i % 5 == 0:
            print('Buzz', end=', ')


def smallest_or_largest():
    winners = [23, 54, 9, 87, 3, 34]

    print('Types "s" to see the smallest number or "l" to see the largest:')
    try:
        user_select = str(input())
        if user_select == 's':
            return find_smallest(winners)
        elif user_select == 'l':
            return find_largest(winners)
        else:
            return 'Something is not quite right!'
    except ValueError:
        print('Please only type s or l')


def find_smallest(numbers:list):
    """
        Iterates the list of values parsed to the function
        to obtain the smallest value.

        params: list of numbers

        return: A string containing the smallest value
    """
    smallest = None  # represents nothing

    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
    
    return f'The smallest value is: {smallest}'


def find_largest(numbers:list):
    """
        Iterates the list of values parsed to the function
        to obtain the largest value.

        params: list of numbers

        return: A string containing the largest value
    """
    largest = None  # represents nothing

    for num in numbers:
        if largest is None or num > largest:
            largest = num
    
    return f'The smallest value is: {largest}'
    

if __name__ == '__main__':
    check_value = smallest_or_largest()
    print(check_value)
    


