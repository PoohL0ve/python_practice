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

## Conditional Executions
Python Boolean values are True and False, in numeric terms they are 1 and 0 respectively. A variable can store a Boolean value as is or using the *is* operator:
```py
flag = True
if flag:
    print("Flag is stunning!")
```
The *bool()* function converts any data type to a Boolean where True is for most values unless they are empty, 0, or the None value. Pythin has three logical operators in and, or and not. __Short circuit evaluation__ is the process of stopping an execution when the truth value is determined.

Conditional statements allow us to check the conditions of a program and change its behaviour. They can be alternative, chained, and nested using *if, elif, and else*:
```py
# Single condition
if x > 0 < 10: print('Positive')
number = 5
number if number % 2 == 0 else 1

# chained statement
value = 11
if value > 5 and value < 10:
    print('Under ten')
else:
    print('Not applicable')

# Nested Conditionals
if number > 0 :
    if number % 2 == 0 :
        print(‘Number is even’)
    else number % 2 != 0 :
        print(‘Number is odd’)
else :
    print(‘Not a number’)
```

## Loops
Loops are repeated forms of code, that is, you can repeat a line of code multiple times based on the number of iterations. Iterations and conditionals form the `control structure` of a program because they determine which lines of code to execute. A loop must have three elements for it to be successful:
1. `Initialisation`: an iteration variable that is declared before the loop starts, which prevents while loops from being inifinite. Sometimes a Boolean True or false may be used with a break point instead.
2. `Condition`: a Boolean expression that determines the next iteration.
3. `Modification`: statements that allow changes to the initialisation variable so that the loop can eventually becomes false.


## Functions

## Strings
Strings are any data that are contained in quotes. They are also immutable objects. To convert strings to lowercase and uppercase the methods `.lower()` and `.upper()` are used. Uppercase letters take precendence over lowercase letters so its best to convert them to the same thing for comparison. The `isupper()` method is a boolean method that checks if all characters in a string are uppercase. Strings can also be multi-lined using `"""`, which is also used for *docstrings* in Python.
```py
my_address = """ 
    Somewhere in Paradise
    with the love of my life.
"""
```
To find the length of a string the `len()` method is used which starts counting from 1. However, to access a character in a string the `[]` notationused used with and **index**, which starts counting from 0. The last character in a string can be obtained by using *len() - 1* in the brackets or the shorthand `[-1]`. Negative indices can also be used to count backwards:
```py
fruit = "mango"
length = len(fruit) #5
last = fruit[length - 1] #o
```

A substring can be created through a process called **slicing** which uses bracket notation and a colon separating values in the form of `[start:end]` which are indices and the *end* value is not included. If the start value is ommitted then it starts checking from 0, while if the end is ommitted it includes the last character.
```py
beauty = "beautiful"
slice_1 = beauty[:5] #beaut
slice_2 = beauty[5:] #iful
# Reverse the string
reverse_beaut = beaut[::-1] #lufituaeb
```
The `in` operator is good to use to check if a substring or a character is in a string: "run" in "Bruno". String can also be transversed using loops.

### Useful String Methods:
A method called is an `invocation` where we are invoking something on a string.

| Methods | Description                   |Example      |
|:-------:|:------------------------------|:-----------:|
|`find`| Takes 3 arguments with the first being the substring or character, the next two are optional which indicates what indices to start and end a search. It returns the index of the first occurence or *-1* if it's not found.| `str.find('u', 1, 4)`|
|`dir`| It is a function that helps us identify what methods can be used on a string| `dir(my_stuff)`|
|`count`| checks the number of times a characters occurs in a string.| `my_hopes.count('a')`|
|`replace`| Takes three arguments with the first one being the value to be replaced, the second the value to replace it with and the third is optional value that specifies how many replacements to make. Without the thrid, all values of the old will be replaced with the new.Can also be chained with multiple replace methods.| `her.replace('wants', 'loves')`|
|`capitalise`| Converts the first character to uppercase and the others to lowercase.| `"title".capitalise()`|
|`title`| converts the first character to uppercase. | `my_str.title()`|
|`strip,rstrip,lstrip`| The methods removes leading whitespace from the string: both sides, right-side, left-side. They can take an argument of any character including special ones to remove.| `my_tea.strip()`|
|`isnumeric, isalpha`| Checks if a strings contains numbers and letters only. |`my_number.isnumeric()`|

### Special Characters
The ‘%’ is used as a formatter when used with a string:
```py
'In %d years I have spotted %g %s.'  % (3, 0.1, ‘camels’) # tuples 
```
The `\n` creates a new line. The `\tab` can be used to add indentation:
```py
print("Shopping list:\n\t- Milk\n\t- Bread\n\t- Eggs")
# Shopping List:
""" - Milk
    - Bread
    - Eggs
"""
print("Loading... \rDone!") # Done!ng...
```
The `\r` is the carriage return which brings something to the start of the line as well as the cursor. The `\` lets us escape characters like double quotes.
