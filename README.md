# Python Programming
Programming is the act of creating computational instructions for a computer to execute. Each language acts as a framework for programmers to constructs their ideas. Programs must be readable, that is, they **must** first be written for humans to understand and then computers to execute. This rule is highly important in collaborative environments.

In simple terms, programming is all about problem solving and there are mechanisms that aid programmers in constructing their ideas:
- __Primitive expressions and statement__ : the simple building blocks the language provides;
- __Means of combination__ : the process in which compound elements are created using simpler ones;
- __Means of abstraction__ : Compound elements can be manipulated.

Programming languages can be defined as formal languages in which strict syntactic rules must be followed. Main elements of programming:
- __Functions__ : rules for manipulating data; can be built-in like *print()* or defined by the programmer;
- __Data__ : the things that programmers want to manipulate.

## About Python
Python is a translated language created by **Guido van Rossum** as a hobby in 1989. The language was developed to be simple and powerful giving Pythonistas a fun language to use. Python is highly used in fields such as Data Science and Analytics, Bio-technology, and AI, although it is powerful and versatile enough to be used in numerous fields including Web Development.

### Reserved Keywords
Reserved keywords are words that cannot be used as variables because Python use them for specific scenarios. There are 32 reserved words in Python as listed in the table:
|      |      |      |      |
|:----:|:----:|:----:|:----:|
|and   |elif |if |pass|
|ass   |else  |import |raise|
|assert |except |in |return|
|break |False |lambda |True|
|class |finally |None |try|
|continue |for |nonlocal |while|
|def |from |not |with|
|del |global |or |yield|

### Python Interpreter
The Python interpreter is what executes the Python script and basic programs. As of October 29th, 2024 the command **python3** opens the interpreter in the command line. The interpreter can be closed using *exit(), quit() or control + D*
Interactive move is used when executing simple expressions in the interpreter, while script mode is used when a file ending in *.py* is created and used.

### Important Programming Terminology
__Comments__ are used to explain a program or some parts of code. It is also a useful way for programmers working on the same project to communicate. Python has two types of comments in single line comments that starts with the *#* symbol and docstrings. Docstrings are used to define a function or a Python program.
```py
# This is a single line comment
"""
    This is a mult-line or doctsring
"""
```

The __syntax__ of a programming language determines how it should be written and breaking this rule results in a *SyntaxError*. This means that the interpreter is unable to understand what the programmer meant.

A __token__ is the simplest element in a program such as a number or variable. An __expression__ is a block of code that can be made up of variables, operators and operands and values that results in a reduced value (determined data type). In other words, the expression is the part of a program that is evaluated when the program is executed. A __block__ is a group of statements that are at the same level of each other, with the head of the block being at the top and the code to be executed is indented. A __statement__ is a group of expressions designed to be executed but not reduced to a value as the expression is the evaluated part.
```py
name = 'python'  # statement
# The example below contains a block of code
for letter in name:  # This is the blcok's header
    # This is the block's body
    add_year = letter + '2024'  # expression
    print(add_year)
```
__Debugging__ is the skill of finding and fixing bugs and errors in code. There are three main types of errors:
- __Syntax Error__ : The rules of the language have been broken;
- __Semantic Error__ : The output of the program is not what was expected or required;
- __Run Time Error__ : Exceptions that occurs after the program runs.
