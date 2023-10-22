queue = input().split()
n = int(input())
index = 0
while len(queue) > 1:
    # Използваме остатък от деление, за да определим детето, което изгаря
    index = (index + n - 1) % len(queue)
    #Придава стойноста на removed_child, от първия елемент на List-a 'queue' и я премахва от него
    removed_child = queue.pop(index)
    print(f"Removed {removed_child}")

winner = queue[0]
print(f"Last is {winner}")