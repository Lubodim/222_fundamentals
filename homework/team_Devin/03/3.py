N = int(input())
teachers = set()
childs = set()

for _ in range(N):
    to_invite = input()
    if to_invite[0].isnumeric():
        teachers.add(to_invite)
    else:
        childs.add(to_invite)

command = input()

while command.lower() != "end":
    if command[0].isnumeric():
        teachers.remove(command)
    else:
        childs.remove(command)

    command = input()

print(len(teachers) + len(childs))

for teacher in teachers:
    print(teacher)
for child in childs:
    print(child)