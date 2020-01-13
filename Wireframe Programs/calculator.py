## simple calculator utilizing functions we've written up until & including 8. Loops.py
## functions present include pickValidNumber, and divByZero

def divByZero(param1, param2):
    try:
        ret = str(param1 / param2)
        return ret
    except ZeroDivisionError as error:
        print(f"Error Caught: {error}\n")

def pickValidNumber():
    while True:
        inp = input("Please enter a number, or enter 'back' to go back to the previous menu: ")
        if inp == "back":
            break
        try:
            num = float(inp)
            return num
        except ValueError as error:
            print(f"Error Caught: {error}\n")

def calculator():
    while True:
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'exp' to raise a number to another power")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input == "add":
            num1 = pickValidNumber()
            num2 = pickValidNumber()
            result = str(num1 + num2)
            print("The answer is " + result + "\n")
        elif user_input == "subtract":
            num1 = pickValidNumber()
            num2 = pickValidNumber()
            result = str(num1 - num2)
            print("The answer is " + result + "\n")
        elif user_input == "multiply":
            num1 = pickValidNumber()
            num2 = pickValidNumber()
            result = str(num1 * num2)
            print("The answer is " + result + "\n")
        elif user_input == "divide":
            num1 = pickValidNumber()
            num2 = pickValidNumber()
            result = divByZero(num1, num2)
            print("The answer is " + result + "\n")
        elif user_input == "exp":
            num1 = pickValidNumber()
            num2 = pickValidNumber()
            result = str(num1 ** num2)
            print("The answer is " + result + "\n")
        else:
            print("Unknown input" + "\n")

def main():
    calculator()

main()
