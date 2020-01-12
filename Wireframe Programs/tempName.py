## retain names/information for immediate processing, delete after usage -- name error for inappropriate mem access

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