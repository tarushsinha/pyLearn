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
print(f"Is the word {pizza} not in the word {greenland}?\n{not pizza in greenland}\n")

## List Functions: append - this method adds an item to the end of an existing list -
sampList = []
## List.append - the dot appears because it is a method of the list class
## see how append works with an empty list
print(f"List is empty: {sampList}. Adding firstObj now")
sampList.append("firstObj")
print(f"List contains: {sampList}\n")

## List Functions: len - this method gets the number of items in the list -
print("Since we added firstObj to the list before, the length of sampList should be 1: ")
print(f"{len(sampList)}\n")

## List Functions: insert - this method is similar to append, but allows insert at any position instead of just the end
sampList = ["Hello", "!"]
sampList.insert(1, "World")
print(f"{sampList}\n")

## More List Functions:
sequence = [1, 2, 4, 5, 5, 8, 9, 20, 5, 100, 150]
print(f"This is the arr: {sequence}")

## index - method finds the 1st occurence of an item and returns its index. returns ValueError otherwise
print(f"The index of 5 is: {sequence.index(5)}")

## max - function that returns list item with maximum value
print(f"The max of sequence is: {max(sequence)}")

## min - function that returns list item with minimum value
print(f"The min of sequence is: {min(sequence)}")

## count - method returns number of occurences of item in a list
print(f"The count of 5 is: {sequence.count(5)}")

## remove - method removes an object from a list
## when multiple of item present, removes first instance of said item
sequence.remove(5)
print(f"The arr after 5 is removed: {sequence}")

## reverse - method reverses objects in a list
sequence.reverse()
print(f"The arr after it is reversed: {sequence}\n")


## List Techniques - List Slicing
## slicing can apply to tuples as well - more on tuples in 1.3 More Types.py
## A more advanced way to retrieve values from a list, list slicing involves indexing a list w/ a start & end index
perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(perfect_squares[2:6])

## if the first index is omitted, it is treated as the smallest
## if the second index is omitted, it is treated as the largest
print(perfect_squares[:5])
print(perfect_squares[5:])

## a third number may be present, representing the step
print(perfect_squares[::2])
print(perfect_squares[2:6:2])

## List Slices can use negative values, which count from the end of the list
print(perfect_squares[1:-1])

## If a negative values is used for the step, the list slice is done backwards - used for reversing a list
print(perfect_squares[::-1])
print(perfect_squares[::1])


## List Techniques - List Comprehensions


