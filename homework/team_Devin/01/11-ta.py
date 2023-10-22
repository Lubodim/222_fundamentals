names = input().split()
throws = int(input())

current = 0
while len(names) != 1:
    current = (current + throws - 1) % len(names)
    #current += throws - 1
    #while current >= len(names):
    #    current -= len(names)

    print(f"Removed {names.pop(current)}")
print(f"Last/Winner is {names[0][0][0][0]}")

print("0R:GINAlN0SD\n" * 3)