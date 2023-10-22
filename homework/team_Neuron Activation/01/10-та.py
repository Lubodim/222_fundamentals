plate_capacity = int(input())
queue = []

while True:
    command = input()

    if command == "End":
        break
    elif command.startswith("refill"):
        refill_amount = int(command.split()[1])
        plate_capacity += refill_amount
    else:
        person_name = command
        bites_requested = int(input())

        if plate_capacity >= bites_requested:
            print(f"{person_name} take bites")
            plate_capacity -= bites_requested
        else:
            print(f"{person_name} must wait")

        queue.append(person_name)

print(f"{plate_capacity} bites left")