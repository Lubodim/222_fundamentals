import os
if os.path.exists("stamat2.txt"):
    os.remove("stamat2.txt")
else:
    print("This file doesn't exist")





#
# try:
#     nums = input("enter nums: ").split(", ")
#     if not nums[0]:
#         raise IndexError("empty list")
#
#     total = sum(map(int, nums))
#     print(total)
#
# except IndexError:
#     print("u can not sum this empty list")
#
# except ValueError:
#     print("u can not sum str")
#









# def divine():
#     try:
#         num1, num2 = map(float, input("num1: ").split(", "))
#
#         result = num1 / num2
#
#         print(f"result {result}")
#
#     except ValueError:
#         print("ne se deli na str")
#     except ZeroDivisionError:
#         print("ne se deli na 0")
# divine()
