## function that returns age classification based on input

def legality(age):
    if age < 18:
        print("underage")
    elif age >= 18:
        if age < 21:
            print("adult, below drinking age")
        elif age < 65:
            print("adult")
        else:
            print("senior citizen")

legality(12)
legality(20)
legality(25)
legality(85)