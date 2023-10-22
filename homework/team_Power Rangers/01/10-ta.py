from collections import deque
starting_bites = int(input())
eaters = deque()

while True:
    name = input()
    eaters.append(name)
    if name == 'Start':
        for i in range(len(eaters) - 1):
            wanted_bites = int(input())
            if starting_bites >= wanted_bites:
                starting_bites = starting_bites - wanted_bites
                person_wants = eaters[0]
                print(f"{person_wants} takes bites")
                eaters.popleft()
            else:
                person_wants = eaters[0]
                print(f"{person_wants} must wait")
                eaters.popleft()
                refill = wanted_bites
                print(f"refill {refill}")
    elif name == "END":
        print(f"There are {starting_bites} bites left.")
    else:
        continue