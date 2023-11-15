def track_parking(n):
    parking_lot = set()

    for _ in range(n):
        entry_exit, car_number = input().split(', ')

        if entry_exit == 'in':
            parking_lot.add(car_number)
        elif entry_exit == 'out':
            if car_number in parking_lot:
                parking_lot.remove(car_number)

    if parking_lot:
        for car in parking_lot:
            print(car)
    else:
        print("Parking is Empty")


n = int(input())

track_parking(n)