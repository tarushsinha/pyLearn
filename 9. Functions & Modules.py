## Functions & Modules

## Code Reuse - Increasing the code size makes it harder to maintain (more to comb through)
## DRY Principle - Don't Repeat Yourself

## Functions - Any statement that consists of a word followed by information in () is a function call

## example functions we've used already -
func = "function"

print("the print function")
print(f"the len function: {len(func)}")
print(f"{list(range(10))}\n")

## the words prior to the () are the function names, comma-separated values are the function arguments
## To define your own function, use `def` -
def sampleFunc():
    print("Hello World\n")

sampleFunc()

## the print statement above is only executed when the function is called
## in the same vein, functions must be defined before they are called, similar to variables


## sample function w/ two params -
def sittingInATree(thingOne, thingTwo):
    print(f"{thingOne} & {thingTwo} sitting in a tree, K-I-S-S-I-N-G")

## Function arguments can be used as vars inside the function definition, but not outside the function's definition -
sittingInATree("David", "Mary")
try:
    print(thingOne)
except NameError as error:
    print(f"Out of Scope - {error}\n")

## Return Statements - this type of statement returns a value that can be used later
def add(a, b):
    return a + b
    print("This statement will never print")

## notice, the print statement within the add function will never execute due to the return prior to it
## returns can only be used from within functions
print(f"{add(2, 4)}\n")

## Comments - annotations to code that make it easier to understand - don't affect how the code is run
## these are examples of comments in python, using a single `#` to initiate the comment, I use 2 for visual formatting
## Python doesn't have multiline commenting functionality, unlike languages like C & Java

## Docstrings - (documentation strings) serve a very similar purpose to comments - designed to explain code
## Created by putting a multiline string containing an explanation of the function below the function's first line -
def docString():
    """
    This is a sample of a docstring, which will not print and simply serves to visually aid the reader in understanding
    the purpose of this function.

    Unlike conventional comments, docstrings are retained throughout the runtime of the program - allowing the
    programmer to inspect these types of comments at run time
    """
    print("Goodbye\n")

docString()

## Functions as Objects
## Though created differently from normal variables, functions are like any kind of value
## They can be assigned and reassigned to variables, and later referenced by those names -
def alert(message):
    print(f"ERROR OCCURED: {message}\n")

## By setting systemCommand = alert, I can use the name systemCommand to call the alert function
a = "Engine broken"
systemCommand = alert
systemCommand(a)

## Functions can also be used as the arguments of other functions -
def concat(a, b):
    return str(a) + str(b)

def runBack(function, a, b):
    return function(function(a,b), function(a,b))

a = 5
b = 10
print(runBack(concat, a, b))
## run the above add function twice
print(runBack(add, a, b))

## Modules - pieces of code that others have written to fulfill common tasks
## Examples of these are random number generation, mathematical operations, etc.
## Remember DRY Principle - Don't Repeat Yourself - this applies to existing code. Don't reinvent the wheel

## Basic usage of modules is to import said module, then use its functions in code -
## print 10 random numbers between 0 - 100:
import random

for iter in range(10):
    print(random.randrange(0,101))

## Another kind of import that can be used if you only need the specific function - `from module_name import var` -
## Then, use the var like normal

from math import pi
print(f"\nThis is the value of pi: {pi}")

## To add to the import statement above, we can pass in the import to a variable of our choice with the `as` keyword
from math import e as magic
print(f"I can reference the base of the natural log as magic: {magic}\n")

## To import multiple objects, separate with commas -
from math import sin, cos
print(f"For multiple imports, separate with commas - the sine of pi/2 is {sin(pi/2)} and the cosine of 0 is {cos(0)}\n")

## Trying to import a module that isn't available causes an ImportError
## Realistically, imports should be checked before code is released so this shouldn't be an issue
## This does apply to modules you may have created, so keep track of what you're creating

## Module types: self-written, installed from external sources, and preinstalled
## preinstalled - Python's standard library
## standard library contains modules including string, math, random, socket, json, doctest, unittest, sys to name a few
## standard library tasking ability includes string parsing, data serialization, testing, debugging, maniuplation of
## dates, emails, command line args, and more

## Some standard library functions are written in Python, some are written in C - most are available across platforms
## Third-party Python modules - most are stored on the Python Package Index (PyPI). These are easily installed via pip
## Once installed, pip can install - `pip install name_of_library`. Then simply `import name_of_library` and use away!
## pip commands should be executed via the command line, not the Python interpreter












