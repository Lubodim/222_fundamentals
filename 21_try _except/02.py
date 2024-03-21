class Penka(Exception):
    pass

def sum_func(lst):
    if len(lst) == 1 and type(lst[0]) == str:
        raise Penka
    if not lst:
        raise IndexError
    result = 0
    for i in lst:
        result += int(i)
    return result

my_list = input().split()

try:
    print(sum_func(my_list))
except ValueError:
    print("You can not sum int and str!")
except IndexError:
    print("You can not sum empty list!")
except Penka:
    print("Input is not correct!")

# my_list = ""
#
# if my_list == True:
#     print(True)
# else:
#     print(False)





