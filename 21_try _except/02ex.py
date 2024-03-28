def sum_numbers(numer_list):
    try:
        if not numer_list:
            raise IndexError('You can not sum empty list!')
        total = sum(numer_list)
        return total
    except TypeError:
        return 'You can not sum int and str!'

number_list = map(int, input().split(" "))
result = sum_numbers(number_list)
print(result)