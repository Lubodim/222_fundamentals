n=int(input())
matrix=[[int(x) for x in input().split(',')]for _ in range(n)]
print(sum(matrix[i][i]for i in range(n)))
print(sum(matrix[i][n-i-1]for i in range(n)))