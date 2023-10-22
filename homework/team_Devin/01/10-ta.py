def snack_party():
    obsto = int(input("Enter initial bites: "))
    people = []

    while True:
        name = input("Enter a person's name (or type 'Start' to begin the party): ")
        if name == "Start":
            break
        people.append(name)

    while True:
        command = input("Enter how much they get: ")
        if command == "End":
            break

        if command.startswith("refill"):
            _, added_bites = command.split()
            obsto += int(added_bites)
        elif people:
            name = people.pop(0)
            requested_bites = int(command)

            if requested_bites <= obsto:
                print(f"{name} takes {requested_bites} bites")
                obsto -= requested_bites
            else:
                print(f"{name} cannot take {requested_bites} bites, not enough bites available")
        else:
            print("No more people in the queue")

    print(f"Leftover bites: {obsto}")

if __name__ == "__main__":
    snack_party()