def float_to_input(n):
    return int(n)
number = input()
try:
    if not number:
        raise IOError
    number = float(number)
    print(float_to_input(number))
except ValueError:
    print("you can not make string to integer")
except IOError:
    print("input must be something ")