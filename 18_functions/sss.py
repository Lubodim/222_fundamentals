def grade(num):
    if 2 <= num <= 2.99:
        return "Fail"
    elif 3.00 <= num <= 3.49:
        return "Poor"
    elif 3.50 <= num <= 4.49:
        return "Good"
    elif 4.50 <= num <= 5.49:
        return "Very Good"
    elif 5.50 <= num <= 6.00:
        return "Excellent"


user_grade = float(input())


def print_func():
    print(grade(user_grade))

print_func()