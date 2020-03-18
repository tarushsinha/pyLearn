## More Types, Data Structures, etc

## the `None` object - represents absence of value - null in other languages
## When converted to a Boolean, represented by False, similar to other empty values (0, [], "")
## When printed w/ `print`, displayed as an empty string ""
None == None
print(None)

## None is returned by functions that don't explicity return anything else
def printOdds(startIndex, EndIndex):
    pList = []
    for num in range(startIndex, EndIndex + 1):
        if num%2 == 1:
            pList.append(num)
    print(pList)

printOdds(10,19)
p = printOdds(0,100)
assert p == None

## Dictionaries - A Data Structure used to map arbitrary keys to values
## functionally, lists can be thought of as dictionaries with integer keys within a certain range

## Every element in a dictionary is represented by a key-value pair
## Dictionaries can be indexed in the same way as lists, using square brackets containing keys (similar to hash in Ruby)
agesDict = {"Alice": 18, "Bob": 21}
combinedAge = agesDict["Alice"] + agesDict["Bob"]
print(f"The combined ages of Alice and Bob is {combinedAge}\n")

## Attempting to access or index a key that isn't part of the dictionary returns a KeyError
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

try:
    print(primary["red"])
    print(primary["yellow"])
except KeyError as e:
    print(f"Error, Invalid Key: {e}\n")

## As observed, dictionaries can store any types of data as values
## empty dictionaries are defined as {}

## Dictionaries - Keys
## Only immutable objects can be used as keys to dicts - i.e.: ones that can't be changed.

## using a mutable object as a key for a dict causes a TypeError
try:
    badDict = {agesDict: "1, 2, 3"}
except TypeError as e:
    print(f"TypeError: {e}")

## similar to working with lists, keys can be assigned to different values
## new keys (that didn't previously exist) can also be assigned values
perfect_squares = {1:1, 2:4, 3:9, 4:"uncalculated"}

## these will be inserted into the perfect squares dictionary, and update the value of 4's perfect square
perfect_squares[4] = 16
perfect_squares[5] = 25
perfect_squares[6] = 36
perfect_squares[7] = 49
perfect_squares[8] = 64
perfect_squares[9] = 81
print(perfect_squares)

## To determine key membership, we can use `in` and `not in`
print(7 in perfect_squares)
print(10 in perfect_squares)
print("eight" in perfect_squares)
print(8 in perfect_squares)

## Method to retrieve dictionary values is get - same thing as indexing but if the key isn't found, returns another val
print(perfect_squares.get(9))
print(perfect_squares.get(10))
print(perfect_squares.get(10, "not in dict"))

## Tuples - similar to lists, except that they are immutable `()`
## Tuples, also similar to lists and dicts can be nested within each other
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z")

## Tuples can be created without `()`
numPad = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for num in numPad:
    print(num)

for i in range(0,len(numPad)):
    print(numPad[i])

try:
    alphabet[1] = "B"
except TypeError as e:
    print(f"Can't change the alphabet\n")

## Numeric Functions -
## min/max of number or list, use `max()` or `min()`
print(min(alphabet))
print(max(alphabet))
print(min(numPad))
print(max(numPad))

## absolute value - `abs()`
print(abs(-42))

## sum - `sum()`
print(sum(numPad))



