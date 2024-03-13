class Spiridon(Exception):
    pass



def something(n):
    for i in range(n):
        if i == 2:
            raise Spiridon("I o6te kak")
        if i == 5:
            raise ValueError("Invalid number")

    return "fun"

try:
    print(something(10))
except ValueError as e:
    print("Mnogo losho - ", e)
except Spiridon as me:
    print("Towa e qko - ", me)
except NameError:
    print("This name dosent exist")
else:
    print("function works correctly")
finally:
    print("That was for now")
