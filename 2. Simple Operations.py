## Basic Concepts

## basic math operations in Python -

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
        print(f"The division of {param1} by {param2} gives us {ret}\n")
    except ZeroDivisionError as error:
        #Output expected error -
        print(f"Error Caught: {error}\n")

## Try DivByZero with 2/2 vs. 2/0
divByZero(var, var)
divByZero(var, 0)

## More fun with division - Isolating Quotient & Remainder

## to circumvent float calculation of int/int, use floor division:
def floorDiv(param1, param2):
    ## Retaining Div by 0 conditional
    try:
        ret = int(param1 // param2)
        print(f"The floor division of {param1} by {param2} gives us {ret}\n")
    except ZeroDivisionError as error:
        #Output expected error -
        # logging.warning(error)
        print(f"Error Caught: {error}\n")

## Try FloorDiv with 5 // 2, 2 // 0
floorDiv(var+3, var)
floorDiv(var, 0)

## to isolate the remainder, simply utilize the modulo operator:
def mod(param1, param2):
    ## Retaining Div by 0 conditional
    try:
        ret = int(param1 % param2)
        print(f"The remainder of {param1} divided by {param2} gives us {ret}\n")
    except ZeroDivisionError as error:
        # Output expected error -
        # logging.warning(error)
        print(f"Error Caught: {error}\n")

## Try modulo with 5 % 2, 2 % 0
mod(var+3, var)
mod(var, 0)

## Exponentiation
def exp(param1, param2):
    ret = param1 ** param2
    print(f"The result of {param1} to the power of {param2} is {ret}\n")

## Try exponentiation with 2^2 & 2^0
exp(var, var)
exp(var, 0)


## Type Conversion

## can convert using int() float() str()
## by casting the result of string concat as an int, the return should be 34 of type int
v1 = "3"
v2 = "4"

ret = int(v1+v2)

print(ret)
print(type(ret))

## Type Conversion can be applied to User Input, see 3. Strings & Manipulation.py for some more input basics
## if we are explicity looking for numbers (ints or floats), we can pre-cast the input (which is a string)
## this method will cause an error when passed non-integer or float values

## simple function to parse user input to only allow for numbers to be input
def parseNumber():
    flag = True
    while flag:
        try:
            num = float(input("\nPlease enter your favorite number whole number/decimal number: "))
            flag = False
            print(f"Your favorite number is {num}\n")
        except ValueError as error:
            print(f"Error Caught: {error}\n")

parseNumber()

## In-Place Operators

## In-place operators allow us to write statements such as x = x + 2, x = x * 2 more concisely -
def inPOpsExample():
    x = 5
    print(x)
    x *= 2
    y = x
    print(f"{y}\n")

inPOpsExample()

## In-Place operators like += work for strings as well -
str = "UM"
print(str)

str += " Terps\n"
print(str)