n = int(input())
invitations = set(range(1, n + 1))

while True:
    command = input()
    if command == "END":
        break

    invitation_number = input(command)

    if invitation_number in invitations:
        invitations.remove(invitation_number)

missing_guests = sorted(invitations)
teachers_missing = [guest for guest in missing_guests if str(guest)[0].isdigit()]

if missing_guests:
    print(len(missing_guests))
    print("\n".join(map(str, missing_guests)))
else:
    print("Everyone attended the party!")

if teachers_missing:
    print(len(teachers_missing))
    print("\n".join(map(str, teachers_missing)))
else:
    print("All teachers attended the party!")