a = int(input())
matrix = []
for i in range(a):
    matrix.append([])
    for j in range(a):
        matrix[i].append(a)
print(*matrix , sep="\n")
