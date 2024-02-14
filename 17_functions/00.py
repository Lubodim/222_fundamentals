def odd_func(list_numbers):
    odd_lis = []
    for el in list_numbers:
        if el % 2 == 1:
            odd_lis.append(el)
        print(odd_lis)


numbers = [int(x) for x in input().split(", ")]

odd_func(numbers)
