## Booleans

## Type in python, values are True & False
## Booleans can be created by value comparison - `==` comes to mind
## Note: variable assigning is done with `=`, comparisons done with `==`

## defining booleans
bool1 = True
bool2 = False

if (bool1 == bool2):
    print(bool1)
else:
    print(bool2)

## More comparison operators - `!=` - if two items are not equal, returns True, false otherwise
if (bool1 != bool2):
    print(bool1)
else:
    print(bool2)

## greater than & less than operators also return booleans
## gt/lt operators work for numbers - i.e.: for floats and ints
print("\nThe following print the boolean return of the gt/lt/gte/lte operations:")
print(7>5)
print(7<5)
print(7>=7)
print(9<=8)

## Boolean Logic

## Python's Boolean operators are `and` `or`, and `not`
## `and` requires both conditions to evaluate to true
print("\nExamples of `and` usage - `&&` in Java:")
print(1==1 and 2==2)
print(1==1 and 2==3)

## `or` requires either of the conditions to evaluate to true for it to be true
## if all args eval to false, the statement is false
print("\nExamples of `or` usage - `||` in Java:")
print(1==1 or 2==2)
print(1==1 or 2==3)
print(1==0 or 2==3)

## `not` takes one argument, and inverts it - i.e.: not True = False, not False = True
print("\nExamples of `not` usage - `!` in Java:")
print(not 1==1)
print(not 2==3)
