products = input().split()
order = input().split()
my_dict = {}
for i in range(0, len(products), 2):
    name = products[i]
    quantity = products[i + 1]
    if name not in my_dict.keys():
        my_dict[name] = int(quantity)
for el in order:
    if el in my_dict.keys():
        print(f"We have {my_dict[el]} of {el} left" )
    else:
        print(f"Sorry, we don't have {el} left")
