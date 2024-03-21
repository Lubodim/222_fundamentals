def float_to_int(n):
    return int(n)
number = input()
try:
    if not number:
        raise IOError
    number = float(number)
    print(float_to_int(number))
except ValueError:
    print("You can not make string to integer")
except IOError:
    print("input must be a something")