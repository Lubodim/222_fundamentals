row_col = int(input())
matrix = []

for row in range(row_col):
    user_input = input().split(", ")
    matrix.append(user_input)

print(*matrix, sep ="\n")

real_sum = 0

for row in range(row_col):
    real_sum += int(matrix[row][row])
print(real_sum)