n = int(input())
my_set = set()
for _ in range(n):
    txt = input().split()
    for i in range(len(txt)):
        my_set.add(txt[i])

print(*sorted(my_set), sep="\n")