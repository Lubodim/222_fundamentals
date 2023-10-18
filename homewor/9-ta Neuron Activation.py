queue = []

while True:
    command = input()

    if command == "END":
        remaining_people = len(queue)
        print(f"{remaining_people} people remaining.")
        break
    elif command == "PAID":
        while queue:
            print(queue.pop(0))
    else:
        queue.append(command)
