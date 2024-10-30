"""
    This module uses examples of variables, getting input from
    the user and different ways to use print statements
"""
# Simple variable
message = 'Welcome to Python!'
#print(message)
# Use str() to ensure the user enters a name
prompt = 'Enter your name: '
#print(prompt)
#your_name = str(input())

# Print using f-string
#print(f'Hello, {your_name}')

drinks = ['whisky', 'magarita', 'beer', 'water', 'soda']
print(*drinks, sep=',')

print('Hello', 'You', 'I know your are', 65, 'years old!')

number = 56.78235
print(f'The decimal is {number:.2f}')