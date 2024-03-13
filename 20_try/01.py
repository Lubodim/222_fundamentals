def my_func(my_lst):
    int_list = []
    for el in my_lst:
        try:
            int_list.append(int(el))
        except ValueError:
            raise ValueError("This list must include only numbers")
    return int_list


my_data = input().split(", ")

int_data = my_func(my_data)
try:
    print(int_data[11])
except IndexError:
    print("Too big index for this list")
except ValueError:
    print("This list must include only numbers")
