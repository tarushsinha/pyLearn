## Exceptions

## We've encountered/touched on exceptions already!

## Examples of this are in trying to convert input of incorrect format to numbers, attempting to divide by zero, etc.
## An exception is an event that occurs as a result of incorrect code/input

## Types of Exceptions include -
## ImportError - failed import
## IndexError - IndexOutOfBoundsException from Java
## NameError - unknown/unnamed variable is used
## SyntaxError - inability to parse code properly
## TypeError - when a function is called on an inappropriate type, `len(1) for example - integers don't have length`
## ValueError - when a function is called on the correct type, but with an inappropriate value

## There is also a hierarchy to consider - https://airbrake.io/blog/python-exception-handling/class-hierarchy
## That link has more information on the error hierarchy. This can be important because specificity when isolating
## errors is a good thing. It means you know what is going wrong for starters!

## Exception Handling -
## when an exception is expected, code can be called within a try/except block - similar to try/catch in Java

## the `try` block contains the code that might throw the exception. Once the exception occurs, try block code stops
## the code then moves from the halted `try` block to the `except` block, where its' code is run.
## the `except` block will never run if no error occurs in the `try` block

## Example of exception handling can be seen in 2. Simple Operations.py in the method divByZero()

## except statements w/out a specified exception will catch all errors(don't do this) - as it hides programming mistakes
## try statements can have multiple except blocks for different kinds of exceptions, or put into a single except block:
## SOLOLEARN example -
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred\n")

## to have code run irrespective of the errors, the `finally` statement is your friend!
## `finally` always goes at the bottom of a try/except block
## if we modify the code from above -
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Jeepers!")
finally:
    print("I run no matter what summons me!\n")

## Raising Exceptions - this can be done with the `raise` statement
def raiseE():
    try:
        print("Sending Value Error\t-")
        raise ValueError
        print("This isn't going to go the way I think huh")
    except ValueError:
        print(f"Error Caught: {ValueError}")
    finally:
        print("I just sent and caught my own error, I'm a bug catcher!\n")

## last print will not print ("...not going to go the way I think huh") -
raiseE()

## Raising Exceptions - exceptions that are raised can be given arguments to provide more detail:
def raiseE(msg):
    print("Sending Value Error\t-")
    raise ValueError(msg)

raiseE("I'm an intentional bug!!!")

## In except blocks, `raise` can be used without args to re-raise the exception
