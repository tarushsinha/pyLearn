## Assertions - `assert`

## sanity-check that can be used while testing
## if the result of an expression is false, an AssertionError is raised

## assertions can take a second argument that is then passed to the AssertionError and raised if the assertion fails

## AssertionError exceptions can be caught and handled like any other exception using the try-except statement,
## but if not handled, AssertionErrors will terminate program execution

## sample program to build, then test using assert to match up inputs correctly!
## program will reverse a number - 18 becomes 81, 19 because 91, etc.
def reverse(inp):
    ret = list(str(inp))
    ret.reverse()
    v = ""
    for i in ret:
        v = v + i
    return int(v)

## valid assertions
assert reverse(81) == 18
assert reverse(18) == 81
assert reverse(11) == 11

## false assertion
assert reverse(21) == 21, "Not the reverse"




