## app that mimics basic fortune teller, minimal options

import random

def fortuneTeller():
    menu = """      Discover your Fortune:
1. What is in store today?
2. What is in store tomorrow?
3. What is my lucky number?
4. Exit Fortune Teller
    """
    while(True):
        print(menu)
        inp = float(input("Which option would you like to choose? "))
        if inp == 1 or inp == 1.:
            print("Today is looking good partner\n")
        elif inp == 2 or inp ==2.:
            print("Tomorrow is uncertain, try asking for the daily fortune tomorrow :)\n")
        elif inp == 3 or inp ==3.:
            rand = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            if rand%2 == 0:
                print("Your lucky number is actually unlucky\n")
                continue
            else:
                print(rand)
        elif inp == 4 or inp ==4.:
            print("exiting gracefully\n")
            break
        else:
            print("Please enter a valid choice\n")

fortuneTeller()