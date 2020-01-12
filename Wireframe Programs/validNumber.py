## function to validate user input as int or floating point number -- catches errors

def validNumber():
    flag = True
    while flag:
        try:
            num = float(input("\nPlease enter your favorite number whole number/decimal number: "))
            flag = False
            print(f"Your favorite number is {num}\n")
        except ValueError as error:
            print(f"Error Caught: {error}\n")

validNumber()