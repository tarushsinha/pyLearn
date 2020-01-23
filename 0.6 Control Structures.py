## Control Structures

# imports
import random
#

## if - conditionals

## if the condition holds, code will run
## sample syntax - Python uses indentation to delimit code blocks - mandatory convention that replaces {} in C
stmt = True
if stmt:
    print("I run if the if-conditional is true\n")

## another sample if statement, with indentation
print(stmt)
if 10>5:
    stmt = False
    print(f"{stmt}\n")

## elif - conditionals

## elif statements are short for else if, useful when chaining if & else statements
## a series of if & elif statements can have a final else block, which is called if none of the if/elif blocks are True
def touch(sense):
    if sense == "hot":
        print("ouch that's hot")
    elif sense == "cold":
        print("brr I'm freezing")
    else:
        print("this is comfortable")

## test above function with different inputs
touch("hot")
touch("cold")
touch("lukewarm")
touch("not even a sense")

## else - conditionals

## else statements follow if statements. They contain code which executes if the if statement evaluates to False
if stmt == True:
    print("\nI execute if the if-conditional is true\n")
else:
    print("\nIf the if-statement is false, this else will always execute\n")

## nested checks - if/elif/else statements can be nested to see if certain/multiple conditions are satisfied -
def legality(age):
    if age < 18:
        print("underage")
    elif age >= 18:
        if age < 21:
            print("adult, below drinking age")
        elif age < 65:
            print("adult")
        else:
            print("senior citizen")

## test above function with different inputs to see how the conditions are satisfied
legality(12)
legality(20)
legality(25)
legality(85)

## while Loops

## where if statements only execute if the condition evals to True, whiles can be run multiple times
## as long as the condition holds, the statements inside the while loop can be repeatedly executed
## once the condition evals to False, the code following the while loop executes
## if the condition is always True, the loop never exits resulting in an infinite loop

## example with variable counting from 1 to 5, then terminating
def whileExample():
    i = 1
    while i < 5:
        print(f"i now equals {i}")
        i += 1
    print(f"i now equals {i}, loop has been terminated\n")

print("\nWhile loop example: ")
whileExample()

## ending loops early -- break statement

## when the `break` statement is encountered inside a loop, the loop finishes immediately -
## using the break statement outside of a loop causes an error

## `continue` - unlike break, this statement jumps back to the top of the loop rather than stopping
## using the continue statement outside of a loop causes an error

## example program utilizing continue & break -
def fortuneTeller():
    menu = """      Discover your Fortune:
1. What is in store today?
2. What is in store tomorrow?
3. What is my lucky number?
4. Exit Fortune Teller
    """
    while(True):
        print(menu)
        inp = float(input("Which option would you like to choose? "))
        if inp == 1 or inp == 1.:
            print("Today is looking good partner\n")
        elif inp == 2 or inp ==2.:
            print("Tomorrow is uncertain, try asking for the daily fortune tomorrow :)\n")
        elif inp == 3 or inp ==3.:
            rand = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            if rand%2 == 0:
                print("Your lucky number is actually unlucky\n")
                continue
            else:
                print(rand)
        elif inp == 4 or inp ==4.:
            print("exiting gracefully\n")
            break
        else:
            print("Please enter a valid choice\n")

fortuneTeller()

## Range
## the range function creates a sequential list of numbers, can be modified to include increments of a number(step)

## the list cast is required because range creates a new object, and must be converted to a list if to be used like one
## more on lists in 0.7 Lists.py

## sample syntax - range(start, end, step)
## Java comparison -> for i = start; i < end; i+=step
evens = list(range(0, 10, 2))
odds = list(range(1, 10, 2))
all = list(range(10))

print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"All: {all}")