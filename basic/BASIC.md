# Fundamental Rules in Python
This repo explains the basics of programming in Python.

## Variables and Getting User Input
Variables are names used to bind information (values). In Python the assignmment operation (=) is used to store the value in a variable. There are a few rules to follow when naming variables in Python:
- Variables must be descriptive (mnenomic), that is, it describes what value the variable binds;
- Variable names can contain letters, the underscore symbol and numbers but it can only start with a letter;
- Use snake_case for simple variables and functions, CONSTANTS for values that won't be changed, and CamelCase for classes.

Global variables are created outside the body of a function or statement and can be used anywhere, while local variables are created in the body of a function or statement and are only accessed there. The *global* keyword allows a global variable to be explicitly used inside a function and a local variable to be used outside of it.

User input can be obtained in the command line by using the built-in *input* function.
```py
# Multiple variables can be created on a single line
fruit, year = 'grapes', '2024'  # String values
your_name = str(input)
print(f'{your_name} favourite fruit is {fruits} for the year {year}')
```

## Print Statement Formatting
The *print()* function is a Non-pure function that returns __None__ but displays any argument parsed to it. By default the function prints information on a newline, however, the *end* argument can be used to specify whether or not to append something to the end of the line with a given delimiter. The separator *sep* argument can be used to specify the delimiter for the arguments being passed. 
Print statements can be formatted using the *+* operator, commas, and f-strings:
```py
# Using the + operator: Can only work on strings
print('This' + 'is' + 'life')

# Using commas: allows different data types
print('Hello', 'You', 'I know your are', 65, 'years old!')

# Using f-strings
number = 56.78235
print(f'The decimal is {number:.2f}')
# The decimal is 56.78
```
Fun fact: The "*" infront of a list being passed to a print() function will display the elements without the brackets.
```py
drinks = ['whisky', 'magarita', 'beer', 'water', 'soda']
print(*drinks, sep=',')
# It prints: whisky,magarita,beer,water,soda
```

## Operators and Operands
Operators are the symbols used to do the computations and the operands are the values the operators are being used on. Python has 7 types of operators:
1. __Arithmetic Operators__ : Used for Mathematical computations and include:
    - + : Used for addition and string Concatenation;
    - - : Used for substraction;
    - * : Multiplication and string repetition;
    - / : Float division;
    - // : Floor division, returns an integer;
    - % : Modulus, retruns the remainder;
    - ** : Exponentiation.
2. __Assignment Opertators__ : Assigns a value to a variable:
    - = : Binds a values;
    - *= : Multiplies a value to another and store it;
    - += : Adds and stores;
    - -= : Substracts and stores;
    - ^= : 
3. __Relational Operators__ : Used to compare values and includes ==, !=, >, >=, <, and <=
4. __Identity Operators__ : Compares objects of the same memory location using *is* and *is not*
5. __Membership Operators__ : Tests if an item or object is contained in a sequence using *in* and *not in*
6. __Bitwise Operators__ : Used to compare Binary values such as:
    - & : AND returns True if both are True;
    - | : OR returns True if either are True;
    - ^ : XOR Exclusive OR, ONLY ONE has to be True;
    - ~ : NOT Negates the values;

The precendence of operators follows the PEDMAS rule with the logical operators having the lowest precedence.
