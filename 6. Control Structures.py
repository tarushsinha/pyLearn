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

## Lists - Python object to store an indexed list of items. Created using square brackets with commas separating items
## list index starts at 0
wordList = ["Hello", "world", "!"]
print(wordList[0] + " " + wordList[1])

## empty lists are created with an empty pair of square brackets -
empty_list = []
print(f"The populated list looks like {wordList}, while the empty list looks like {empty_list}\n")

## List - data types
## Typically, a list will contain items of a single item type, but it is also possible to include different types
## Lists can also be nested within other lists - think 2d array

## Sample iterate through 2d array when unsure of item types being stored -
arr2d = ["Hello", "World", 0, [1, 2, 3], [4, 5, 6]]
for item in arr2d:
    if type(item) == type(arr2d):
        for cmpnt in item:
            print(cmpnt)
    else:
        print(item)

## Strings representation - indexed as lists. Indexing strings behaves as though you are indexing chars in the string
## Being indexed like a list is a String property, cause a TypeError with integers and other types

## two example - printing strings character by character
## example one
word = "pneumonoultramicroscopicsilicovolcanoconiosis"
sb = ""
for char in word:
    sb = sb + char + " "

print("\nLongest word in the English language at 45 letters: ")
print(sb)

## example two
thirdWord = "floccinaucinihilipilification"
sb = ""
for i in range(len(thirdWord)):
    sb = sb + thirdWord[i] + " "

print("\nThird longest word in the English language at 29 letters: ")
print(sb)

## List Operations - items at a certain index in a list can be reassigned
ages = [12, 19, 20, 85]

## replace the 20 year old with a 25 year old
ages[2] = 25
print(f"\nAges List: {ages}\n")

## Lists can be added & multiplied in the same way as strings -
print(ages + [14, 18, 20])
print(ages * 3)

## To check List membership, the `in` operator can be used to return a Boolean value
## If the item occurs at least once in the list, Boolean returns True, False otherwise
print(f"\nIs there a 21 year old in the ages pool?")
print(21 in ages)

## Uses of `in` can be extended to a simple substring checker
## This method ignores python's case sensitivity
def substring(word, substring):
    if substring.lower() in word.lower():
        return True
    else:
        return False

Australia = "Australia"
trail = "trail"
print(f"\nIs the word {trail} in the word {Australia}?\n{substring(Australia, trail)}\n")

Barbie = "Barbie"
barb = "barb"
print(f"Is the word {barb} in the word {Barbie}?\n{substring(Barbie, barb)}\n")

## Similar to how we used `not` to negate the value of variables, we can check the opposite of `in`
pizza = "pizza"
greenland = "greenland"
print(not pizza in greenland)