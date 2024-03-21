
def check(other_names, names):
    people_ages = []
    for name in other_names:
        people_ages.append(names[name])
    return people_ages

names = {}

list1 = input().split()
for i in range(0, len(list1), 2):
    names[list1[i]] = int(list1[i+1])

other_names = input().split(", ")

try:
    print(*check(other_names, names), sep=", ")
except KeyError:
    print("This person does not exist in this dictionary")
else:
    print("That was ages of the persons")