num1, num2 , op = [float(x) if x.isdigit() else str(x) for x in input().split()]
if op == "+":
    result = lambda x, y: x + y
elif op == "-":
    result = lambda x, y: x - y
elif op == "*":
    result = lambda x, y: x * y
elif op == "/":
    result = lambda x, y: "You can not divide by zero" if y == 0 else x / y

print(result(num1, num2))