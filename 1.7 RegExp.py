## Regular Expressions
## --> Powerful tool for string manipulation

## Useful for pattern matching, and string substitutions

## Regular expressions in Python can be accessed with the `re` module
import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("match")
else:
    print("no match")