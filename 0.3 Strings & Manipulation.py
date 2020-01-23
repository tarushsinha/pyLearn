## Strings & Manipulation

## Strings are created by entering text between " " or ' '. Console displayed output for Python strings is ' '.
s = "Hello World"
print(f"Variable s is of type: {type(s)} and says {s}\n")

## Some characters can't be displayed directly in a string - examples are double quotes, newlines, backslashes
## Backslashes('\') are used to escape tabs, arbitrary Unicode characters to name a few. Known as escape characters
tyrion = "\n\"Never forget what you are, the rest of the world will not. Wear it like armor and it can never be used to " \
         "hurt you\" \n \t- Tyrion Lannister to Jon Snow, A Song of Ice & Fire"
print(f"Here is an example of a String with quotes, and escape characters: {tyrion}\n")

## Avoiding \n in Syntax -
## Utilize three sets of quotes, newlines created by pressing Enter, tabs, etc. are interpreted as escaped - """ """
haiku = """
    \"The Old Pond\" by Matsuo Bashō
        An old silent pond
    A frog jumps into the pond-
        Splash! Silence again.
        """
print("Here is a haiku printed without typing escape characters:")
print(haiku)

## I/O - Input & Output

## Usually programs take input & process to produce output - In python, the print function can produce output -
sb1 = "This is an example of "
sb2 = "print doing string concatenation and returning the result\n"
print(sb1 + sb2)

## print doing stringbuild, along with 2 + 2
sb3 = "Math "
sb4 = "is "
sb5 = "hard"
num = 2

print(sb3 + sb4 + sb5)
print(f"{num} + {num} is {num + num}\n")

## Input - to get user input, use the input() function. The function prompts users for input, then returns as a String

## Prompt for favorite song, then return as a String
song = input("Please enter your favorite song: ")
print(f"The user's favorite song is {song}\n")

## More on Concatenation - strings can be added, joining the two strings:
concatScenario = "Home of the "
concatLocation = "Maryland " + "Terrapins\n"

print("This concatenation example is brought to you by UMD, the " + concatScenario + concatLocation)

## Concat Numbers example -
num1 = "3"
## Also including example of Type Conversion here - casting the String variables as integers
print(f"Int add makes {num1} + {num1} = {int(num1) + int(num1)}. String add makes it {num1 + num1}\n")

## String Operations -
## Strings in python can be multiplied by integers which repeats the original str a # of times. Doesn't work w/ floats

## Printing Hello World 3 times
print(f"{s}\n" *  3)

## Multiplying a String by zero prints an empty line
print(f"{s}\n" * 0)