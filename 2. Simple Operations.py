## imports
import logging
##

## Basic Concepts

## basic math in Python
var = 2

## basic functions to add, subtract, multiply, divide
def add(param1, param2):
    ret = param1 + param2
    print(f"The addition of {param1} and {param2} gives us {ret}\n")

def sub(param1, param2):
    ret = param1 - param2
    print(f"The subtraction of {param1} and {param2} gives us {ret}\n")

def mult(param1, param2):
    ret = param1 * param2
    print(f"The multiplication of {param1} and {param2} gives us {ret}\n")

def div(param1, param2):
    ret = int(param1 / param2)
    print(f"The division of {param1} by {param2} gives us {ret}")
    print("Note: in python3, integer/integer results in a float - we have casted it as an int here to circumvent this\n")

## call above methods, adding, subtracting, multiplying, and dividing var by itself - 2 by default
add(var, var)
sub(var, var)
mult(var, var)
div(var, var)

## In addition to division of two integers resulting in a float, division by zero throws the ZeroDivisionError
## More on ZeroDivisionError: https://airbrake.io/blog/python-exception-handling/zerodivisionerror-2
## More on logging - referenced for error printing: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

## tl;dr: All Python exceptions inherit from the "BaseException" class, or extend from an inherited class therein
## Exception hierarchy for this error is: BaseException -> Exception -> ArithmeticError -> ZeroDivisionError

## modifying the above div method to handle division by zero exception:
def divByZero(param1, param2):
    try:
        ret = int(param1 / param2)
        print(f"The division of {param1} by {param2} gives us {ret}")
    except ZeroDivisionError as error:
        #Output expected error -
        logging.error(error)

## Try DivByZero with 2/2 vs. 2/0
divByZero(var, var)
divByZero(var, 0)

