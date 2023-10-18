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
    