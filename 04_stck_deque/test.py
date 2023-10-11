from collections import deque
my_deque = deque([1, 2, 3, 4, 5, 6, 7, 8])
while my_deque:
    a = my_deque.popleft()
    print(a)
    a += 5
    
    print(a)
    my_deque.appendleft(a)
    a = my_deque.popleft()
