n = int(input())
parking_lot = set()

for _ in range(n):
    operation, number = input("Enter the operation of the car and it's number: ").split(", ").lower()

    if operation == "in":
        parking_lot.add(number)
    elif operation == "out":
        if number in parking_lot:
            parking_lot.discard(number)
        else:
            print("This number isn't in the parking lot")

for n in parking_lot:
    print(n)
if not parking_lot:
    print("The parking lot is empty")
