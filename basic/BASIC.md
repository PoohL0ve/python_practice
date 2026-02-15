# Fundamental Rules in Python
This repo explains the basics of programming in Python.

## Variables and Getting User Input
Variables are names used to bind information (values). In Python the assignmment operation (=) is used to store the value in a variable. There are a few rules to follow when naming variables in Python:
- Variables must be descriptive (mnenomic), that is, it describes what value the variable binds;
- Variable names can contain letters, the underscore symbol and numbers but it can only start with a letter or `_`;
- Use snake_case for simple variables and functions, CONSTANTS for values that won't be changed, and CamelCase for classes.

Global variables are created outside the body of a function or statement and can be used anywhere, while local variables are created in the body of a function or statement and are only accessed there. The *global* keyword allows a global variable to be explicitly used inside a function and a local variable to be used outside of it.

User input can be obtained in the command line by using the built-in *input* function.
```py
# Multiple variables can be created on a single line
fruit, year = 'grapes', '2024'  # String values
your_name = str(input)
print(f'{your_name} favourite fruit is {fruits} for the year {year}')
```
```py
# Check the data type 
print(isinstance(42, (str, bool))) # False
print(type(True)) # Boolean
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
7. __Boolean Operators__:
    - _and_: x and y
    - _or_: x or y
    - _not_: not x

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

The `range()` function can take three arguments:
- *first*: where to start counting
- *second*: where to stop not inclusive
- *third*: skip numbers

The `for` loop is best used when the number of elements in the item or set is known. It uses an *iteration variable*, the *in*, and the object to loop through in its header statement to control the flow of the execution of the loop. Additionally, the `_` can be used if the iteration variable isn't going to be used with the *range()* function:
```py
for fruit in fruits:
    # Do something

for _ in range(10):
    # Do something
```

The `while` loop needs a condition that will eventually make it stop as it can easily become infinite. It is best used when the length of items is unknown. The **while** loop can also use the *True or False* values in combination with a break statement. The `break` statement is used to jump out of a loop and thus stop it from iterating, which ends the execution of the body. The `continue` is used to skip an iteration, and not execute the body for it.
```py
while True:
    line = str(input())
    if line == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')
```

Loops can be nested inside other loops and use helper variables to control the loop:
```py
number = int(input('Enter number: '))

while number > 0:
    check_num = 0 # Helper variable
    while check_num < number:
        print(check_num, end="")
        check_num += 1
        print()
    number -= 1
```


## Functions
A function is a named sequence of statements that perform computation in its body. That is, it allows code to be modula and remove repetition as it is a reusable piece of code. In Python the `def` keyword defines a function and the name of the function is followed by parentheses. Inside the parantheses can be parameters that define the type of data needed for a function. These are called `annotations` which are stored in `__annotations__` which provide metadata for functions that tools may use. They do not enforce types but some sort of contract.

If a function uses the `return` keyword, then it returns some type of value which can also be defined in the function's head. If the keyword is not there, then Python will return `None`.
```py
def name_of_function(para1: str, para2: int) -> return_type:
    # Do Something
    # Return Something
```
The **type hints** in the head of the function allows us to avoid errors.

```py
def area(width, length):
    """
    Calculate the area of a rectangle.

    Parameters:
    - width (float): The width of the rectangle.
    - length (float): The length of the rectangle.

    Returns:
    - float: The calculated area of the rectangle, which is the product of the width and length.

    Example:
    >>> area(5, 10)
    50.0
    """
    return width * length

```
__System Thinking__: Type hints describe intent. Validation enforces reality. Context determines responsibility. Validate at the boundary.
```py
# Get the century
def get_century(year: int) -> int:
    # write your code here
    if year == 0:
        return 1

    return (year - 1) // 100 + 1
```
### Arbitrary Arguments
Sometimes the number of arguments that may be needed or passed to a function may be unknown. By adding an `*` before the parameter it allows any number of positional arguments which will placed in a tuple for the function to use.
```py
def add(*nums):
    size = len(nums)
    if size == 0:
        return 0
    total = 0
    for number in nums:
        total += number
    return total
```
By using `**` before a parameter the function will accept any number keyword arguments which will be placed in a dictionary. However, the order of arguments in a function's header is important:
1. __positional arguments__
2. __*args__
3. __Keyword-Only arguments__
4. __**kwargs__
```py
def position(name, date, *args, sale=2, **kwargs):
```
🧠 __Mental Model__: The astericks are used in a functions head to _pack_ arguments, while in the function itself (including built-in), they are used to unpack sequences (*) and mappings (**) respectively. They are important for understanding _decorators_, _dependenncy injection_, _dynamic configuration_, and _CLI argument forwarding_.
```py
# The * forces all parameters to be keyword only
def all_check(*, price, quantity):
```
Additionally, anything before `/` indicates __positional-only__:
```py
def f(a, b, /, c, *, d):
    pass
```
The above design enforces clarity for core parameters (a,b), allowing c to be flexible, prevent mis-binding, maintains backward compatibility with APIs, and communicate intent clearly.

Python also has several built-in functions such as:
- int(), str(), list(), float(), print()
- max(), min(), sum()
- input()
```py
user_name = str(input("Enter your name: "))
```
### Understanding Scope
Python uses the `LEGB` rule to determine the scope of variables in functions and classes:
- __Local Scope (L)__: Variables that are defines within a function or class can only be accessed there.
- __Enclosing Scope (E)__: Allows functions defined inside of another function to access the variables of the parent function.
- __Global Scope (G)__: These types of variables can be accessed anywhere in the program as they are not declared within a function or class. The `global` keyword can allow one to modify a global variable within a function or make a local variable global.
- __Built-in Scope (B)__: Refers to all of Python's modules, built-in functions, and keywords which can be used anywhere in the program.

## Strings
Strings are any data that are contained in quotes. They are also immutable objects, meaning they cannot be modified directly but can be reassigned. To convert strings to lowercase and uppercase the methods `.lower()` and `.upper()` are used. Uppercase letters take precendence over lowercase letters so its best to convert them to the same thing for comparison. The `isupper()` method is a boolean method that checks if all characters in a string are uppercase. Strings can also be multi-lined using `"""`, which is also used for *docstrings* in Python.
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
`String Interpolation` is the process of inserting variables and expressions into string. Formatted string literals (__f-strings__) allow interpolation to be handles easily.
```py
age = 23
info = f'I am struggling with adulthood at the age of {age}'
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
|`split`| Splits the characters of a string into a list by using whitespace as a default delimeter. An Additional argument can be used which to limit the number of splits| `str.split(',', 2)`|
|`startswith, endswith`| Checks if a string starts or ends with a specific sequence or characters or a single character| `str.endswith('early')`|

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


## Lists
Lists are a collection datatype that can contain any type of data. They are also mutable objects that can be created using `[]` or the built-in `list()` function in Python. Elements in the list object can be accessed using the index of the object with bracket notation, additionally, it's the same way elements can be mutated.
```py
numbers : int = [1, 2, 3]
numbers[1] = 8
print(numbers) # 1, 8, 3
odd_nums = list(range(1, 20, 2))
```
A string can be converted into a list by using the *list()* function which splits the characters into elements. The `split()` method can also be used to do the same, with a delimiter argument. The `join()` takes a the list object and turns it into a string by being attached to a delimiter.
```py
", ".join(words)
```
### Common List Methods and Operations
|Method | Description                    | Example     |
|:-----:|:-------------------------------|:-----------:|
|`append`| Adds items at the end of a list.| `shoes.append('Adidas')`|
|`insert`| It takes two arguments, one being the index and the other the element to add at the specified index, where all other elements are pushed to the right.| `shoes.insert(1, 'Nike')`|
|`pop`| Can delete and return the last element if no arguments are given. |`fruits.pop(2)`|
|`remove`| The methods takes the element of the item to be removed as its arguments and removes the first occurence of it. It is best to check if the element is present by using the `in` keyword. If multiple items has to be removed the `del` keyword can be used with bracket notation.| `del food[1:4]`|
|`sort, sorted`| Both methods arranges the elements in ascending other, but *sort()* modifies the original and *sorted()* is used for a new list. The key parameter of *sorted* can take any function including user-defined ones| `sorted(words, key=len)` `names.sort(reverse=True)`|
|`extend`| Appends on list to another by mutating the original | `prime_nums.extend(even_num)`|
|`reverse, reversed`| The *reverse()* returns None, while the *reversed* returns an iterator.| `for number in reversed(numbers)` numbers.reverse()|
|`copy`| Creates a copy of a list. |`names.copy()`|
|`index`| Searches for the first occurence of an element and returns the index. Also have optional start and end arguments. |`days.index(day)`|

The `+` operator concatenates lists, similiar to the `extend()` method but its used for creating a new list, and the `*` operator repeats the elements in a list a given number of times.

The `min()` and `max()` functions determine the minimum and maximum values in a list, while the `sum()` adds all the element of a numeric list. The `all()` function returns **True** if all items in the lists are True, and `any()` returns **True** if atleast one item is True.

