my_set = set()

for _ in range(int(input())):
    my_set.add(input())
command = input()

while command.lower() != "end":
    my_set.discard(command)
    command = input()

print(len(my_set), *sorted(my_set), sep="\n")
