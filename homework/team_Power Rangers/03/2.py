user_input = int(input("Input how many cars will be entering"))

parking_spaces = set()
for i in range(0, user_input):
    parking_input = input("Input the command and the licenese number").split(", ")
    if parking_input[0].upper() == "IN":
        parking_spaces.add(parking_input[1])

    elif parking_input[0].upper() == "OUT":
        parking_spaces.discard(parking_input[1])

if parking_spaces:
    for i in parking_spaces:
        print(i)

else:
    print("Parking is empty")