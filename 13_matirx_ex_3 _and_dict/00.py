# n, m = map(int, input().split(", "))
n, m = [int(i) for i in input().split(", ")]
matrix = []
for _ in range(n):
    matrix.append([int(gosho) for gosho in input().split(", ")])
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
print(n)
print(m)