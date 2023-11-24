# m_list = [[1, 2, 3, 4], [[5], 6, 7, 8], [9, 10, 11, 12]]
#
# print(m_list[1][0][0])
#
# matrix = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 4, "b"],
#     [1, 2, 3, 4],
# ]
#
# print(matrix[2][3])
# rows = 3
# matrix = [[(column + row * 3) for column in range(rows)]for row in range(rows)]
# print(*matrix, sep="\n")

rows = 3
matrix = []
for row in range(rows):
    matrix.append([])
    for column in range(rows):
        matrix[row].append(column + row * 3)
print(*matrix, sep="\n")