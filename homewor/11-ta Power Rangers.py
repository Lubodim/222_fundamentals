stack = [str(x) for x in input().split()]
n = int(input())
counter = 1

while True:
    if len(stack) == 1:
        print(f"{stack[0]} is the winner!")
        break
    else:
        for i in stack:
            if counter == n:
                print(f"{i} is removed")
                stack.remove(i)
                counter = 0
                continue
            else:
                counter += 1
                continue