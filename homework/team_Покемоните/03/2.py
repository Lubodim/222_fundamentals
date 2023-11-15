n = int(input(""))
parking = {}
for _ in range(n):
    entry = input().split(", ")
    action, plate = entry[0], entry[1]

    if action == "IN":
        parking[plate] = True
    elif action == "OUT" and parking.get(plate, False):
        parking[plate] = False

cars_in = [plate for plate, in_parking in parking.items() if in_parking]

if cars_in:
    print("Cars in parking lot:", ", ".join(cars_in))
else:
    print("Parking is empty")
