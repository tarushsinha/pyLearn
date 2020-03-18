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

## String Formatting

## we can use the string's format method to substitute a number of argument into a string
## each arg of the format function is placed into the string at the position corresponding to that determined by the {}
def weatherConverter():
    ## Capture temperature values & unit (F or C)
    while True:
        try:
            num = float(input("What is the temperature outside?: \ "))
            break
        except ValueError as error:
            print(f"Error Caught: {error}\n")
    while(True):
        mode = input("Is that Fahrenheit or Celsius? Enter `F` for Fahrenheit or `C` for Celsius! \ ")
        if mode == 'F' or mode == 'C':
            break

    ## Proces conversion for each
    if mode == 'C':
        num = (num * 9/5) + 32
        mode = "Fahrenheit"
    else:
        num =(num - 32) * 5/9
        mode = "Celsius"

    retMsg = "The temperature outside is {0} degrees {1}".format(num, mode)

    ## String formatting can also be done with named arguments as done below
    ret2Msg = "The temperature outside is {num} degrees {mode}".format(num = num, mode = mode)

    print(retMsg)
    print(ret2Msg)

weatherConverter()

## String Functions

## join() - joins a list of strings with another as a separator
sep = ", "
sJoin = sep.join(["Hello", "World"])
print(sJoin)

## join() can be used to add a space between all letters of a word for example
spc = " "
sepStr = spc.join("cowabunga")
print(sepStr)

## replace() - replaces a substring present in a string with another
print(s.replace("World", "ME\n"))

## startswith() and endswith() determine the presence of a substring at the start & end of a string respectively
## this is similar to the usage of ^ $ in regexp in some ways
myName = "Tarush"
sampleEmail = """To Whom This May Concern:

This is where I would show you I have a lot of important stuff to say. But in the place of that, you're going to get
some good old Lore Ipsum stuff!

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sagittis maximus elit. In sit amet tincidunt nisl. Nunc 
nisl tellus, dignissim congue tempus eu, sollicitudin non magna. Duis pretium sed velit eu condimentum. Nullam malesuada
iaculis mollis. Nam sed iaculis erat. Quisque feugiat ut libero id aliquam. Integer consequat libero sed turpis 
ullamcorper dapibus. Integer eget tortor ac erat interdum egestas ultricies in sapien. Nullam tristique et nunc sed 
bibendum.
 
Best Regards,
{myName}""".format(myName = myName)

def validEmail(msg, name):
    ret = "Valid"
    if not(msg.startswith("Dear")):
        ret = "Fail - bad start"
    if not(msg.endswith(name)):
        if ret != "Valid":
            ret = ret + " and bad end"
        else:
            ret = "Fail - bad end"
    print(ret)

validEmail(sampleEmail, myName)

def shout(strinput):
    return strinput.upper()

print(shout("i swear i'm not angry"))
print(shout("ARE you SURE"))
print(shout("there ARE fourty 2 letters in this SENTENCE...mAyBe"))

def whisper(strinput):
    return strinput.lower()

print(whisper("I'M TELLING YOU A SECRET HERE"))
print(whisper("what happens in Vegas stays in Vegas"))

## common interview question - remove all spaces in a string)
def removeSpace(strinput):
    return strinput.split(" ")

print(removeSpace("This is a list where I have isolated the words!"))

## more string formatting - can be done with named arguments
endGreeting = "{x}, {y}".format(x = "Sincerely", y = "Tarush")
print(endGreeting)

