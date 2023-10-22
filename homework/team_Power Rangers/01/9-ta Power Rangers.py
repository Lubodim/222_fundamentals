from collections import deque
my_queue = deque()
while True:
    client_name = input()
    my_queue.append(client_name)
    if client_name == "END":
        my_queue.pop()
        len_queue = len(my_queue)
        print(f"{len_queue} people remaining.")
        break
    elif client_name == "PAID":
        my_queue.pop()
        for i in range(len(my_queue)):
            print(my_queue[0])
            my_queue.popleft()


#2
#
# stack = []
#
# while True:
#     un_pade = input("Input the customers! ")
#
#     if un_pade == "PAID":
#         for i in range(len(stack)):
#             stack.pop()
#
#     elif un_pade == "END":
#         for i in stack:
#             print(i)
#
#         print(f"{len(stack)} people remaining! ")
#         exit()
#
#     else:
#         stack.append(un_pade)