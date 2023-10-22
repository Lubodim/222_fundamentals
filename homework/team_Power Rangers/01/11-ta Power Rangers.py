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


#2
#
# from collections import deque
#
# names = input("Enter the names of all participants: ").split(' ')
# elimination_count = int(input("Enter the elimination count: "))
#
# participants = deque(names)
#
# while len(participants) > 1:
#     for _ in range(elimination_count - 1):
#         participants.append(participants.popleft())
#     eliminated = participants.popleft()
#     print(f"{eliminated} is eliminated!")
#
# print(f"The winner is {participants[0]}!")