## Working with Files


## Opening Files
## text files are the easiest to manipulate - before editing a file, it must be opened using `open`

## `open` modes
## write mode - `open("path", "w")`
## read mode - `open("path", "r")`
## binary write mode - `open("path", "wb")`
## append mode - `open("path", "a")`

# w+  create file if it doesn't exist and open it in (over)write mode
#     [it overwrites the file if it already exists]
# r+  open an existing file in read+write mode
# a+  create file if it doesn't exist and open it in append mode

## To begin work with a file, it must be opened -
## General syntax of File `open` - `f = open("path_to_file")`
f = open("../WireframePrograms/ideas.txt")
g = open("../WireframePrograms/ideas.txt")
h = open("../WireframePrograms/ideas.txt")

## do work to/with file

## file read() - default param is -1, reads entire file. Param specifies chunks(bytes) of file that should be observed
## subsequent calls to the read function will read more of the file byte by byte (if param specified)
## once file has been read, further attempts to read will return empty strings (reading from EOF)
print(f.read())

## file readlines() - returns a list in which each element is a line in the file
print(g.readlines())

## for-each loop to iterate through lines in the file -
for line in h:
    print(line)

## file write() - writes a string to a file
## for semantics on writing to an uncreated files, overwriting, etc., see above!
## when files are opened in write mode, the existing contents of the file are deleted
## if a file is opened in write mode and then immediately closed, the contents are deleted
ins = open("SelfResources/test.txt", "a+")
## the write method returns the number of bytes written (if successful)
x = ins.write("This has been appended to our created dummy file opened in `a+` mode")
ins.close()

ins = open("SelfResources/test.txt", "r")
print(ins.read())
ins.close()

print(x)

## once work has been done with files, make sure to close them
f.close()
g.close()
h.close()

## Officially working with Files -
## Good practice (and to avoid wasting resources) - is to make sure files are always closed after they've been used
## - this can be accomplished by use of try & finally - ensures file is always closed even with an error
## - remember - this is because finally blocks always execute
try:
    f = open("SelfResources/test.txt", "r")
    print(f.read())
finally:
    f.close()

## another option is to use `with` statements - creates a temporary variable only accessible within indented block
## even if errors/exceptions occur, the file is automatically closed at the end of the `with` statement
with open("SelfResources/test.txt") as f:
    print(f.read())

