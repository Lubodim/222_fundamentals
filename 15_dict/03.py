my_dict = {}
while True:
    command = input()
    if command == 'START':
        break
    name, quantity = command.split(": ")
    if name not in my_dict.keys():
        my_dict[name] = 0
    my_dict[name] += int(quantity)

print("Products in stock:")
for k, v in my_dict.items():
    print(f"- {k}: {v}")

count_key = len(my_dict.keys())
count_value = 0
for v in my_dict.values():
    count_value += v
print(f"Total Products: {count_key}")
print(f"Total Quantity: {count_value}")