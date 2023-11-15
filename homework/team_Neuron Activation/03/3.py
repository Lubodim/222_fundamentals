def party_invitations(n):
    invitations = set(map(str, range(1, n + 1)))

    while True:
        guest = input()
        if guest == "END":
            break

        if guest in invitations:
            invitations.remove(guest)

    teachers_invitations = sorted([invite for invite in invitations if invite[0].isdigit()])
    students_invitations = sorted([invite for invite in invitations if not invite[0].isdigit()])

    print(len(invitations))
    print("\n".join(teachers_invitations + students_invitations))


n = int(input())

party_invitations(n)