def func(a,b):
    return float(a) / float(b)


num1, num2 = input().split(',')

try:
    print(func(num1,num2))
except ValueError:
    print("You can't divide by symbols")
except ZeroDivisionError:
    print("You can't divide by ZERO")