m, n = tuple(map(int, input().split()))
set_m = set()
set_n = set()

for i in range(m):
    set_m.add(int(input()))

for i in range(n):
    set_n.add(int(input()))

print(*set_m.intersection(set_n), sep="\n")
