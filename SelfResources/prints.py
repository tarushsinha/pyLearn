# Prints can use '' or ""
print('Print Examples:')
# \n, \t, etc. can be used within quotes
print("Char Syntax:\n\t\t\tcan do this!\n")

# {} represent Sets, cannot store duplicates. While len(mood) should be 7, it is 6
# more on Sets (basic uses) - membership testing, eliminating duplicate elements
mood = {"sunny", 43, "rainy", "gloomy", "cloudy", "beautiful", "sunny"}
print(f'The type of mood is {type(mood)}.')
print(f'The type of mood is {len(mood)}.')

# [] represent lists
moodList = ["sunny", 43, "rainy", "gloomy", "cloudy", "beautiful"]
print(f'The type of moodList is {type(moodList)}.')

print('Printing the list:')
# unnecessary to iterate through len(list), similar to enhanced for-loop in Java
for i in moodList:
    print(f'This is a {i} day')

