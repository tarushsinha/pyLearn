## Variables

## Variables let you store values by assigning a name to reference it by later in the program

## Variable assigning in python is done with the equals sign -
x = 5
y = 2
z = x * y

print(f"x = {x}" + "\n" + f"y = {y}" + "\n" + f"z = x * y = {z}\n")

## Unlike in other languages where variables have specific types, this is not the case in python
## You can assign a string to a variable, then later assign an integer to the same variable -
print(f"Before, we set x to equal {x}")

## cast as strings, then concat, then cast as int again
x = int(str(x) + str(y))

print(f"We then casted x & y as strings, concatenated and stored the new value into x, making it {x}\n")

## Variable naming -

## Python is a case sensitive programming language
X = 7
print(f"x = {x} and X = {X}, x + X = {x + X}\n")

## Only characters that are allowed are letters, numbers & underscores. Variables can't start w/ numbers
## Variables, classes, etc. can be removed using the `del` statement. This removes reference from the name to the value

## sample function that only retains input name for short period of time
def tempName():
    flag = True
    while flag:
        try:
            tmpName = input("Please enter your name for temporary processing, type `exit` to exit: ")
            if tmpName == "exit":
                flag = False
            else:
                print(f"Nice to meet you {tmpName}\n")
                del(tmpName)
                print(f"We will now try to print your name to show we have not stored it: {tmpName}")
        except NameError as error:
            print(f"No name stored on file. Full error: {error}\n")

tempName()


