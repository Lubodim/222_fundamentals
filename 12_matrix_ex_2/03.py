n = int(input())
matrix = []

for row in range(n):
    current_row = input().split(', ')
    matrix.append(current_row)
for row in matrix:
    print(*row, sep = ', ')
