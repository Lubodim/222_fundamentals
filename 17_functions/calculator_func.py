def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "U can not divide by ZERO"
    return num1 / num2


def main_func():
    while True:
        number1 = float(input("ENTER first number: "))
        number2 = float(input("ENTER second number: "))
        operator = input("Choice between + - * / or Stop for END.: ")
        if operator.lower() == "stop":
            break
        elif operator == "+":
            result = add(number1, number2)
        elif operator == "-":
            result = subtract(number1, number2)
        elif operator == "*":
            result = multiply(number1, number2)
        elif operator == "/":
            result = divide(number1, number2)
        else:
            print("invalid operator!")
            continue
        return result

print(main_func())
