class_222 = {}
data = input().split()

for i in range(0, len(data), 2):
    name = data[i]
    number = data[i + 1]
    if name not in class_222.keys():
        class_222[name] = int(number)

print(class_222)