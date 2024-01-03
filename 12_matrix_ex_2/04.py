rows = int(input())
# matrix = []
totol_sum = 0
for r in range(rows):
    # current_row = list(map(int, input().split(", ")))
    current_row = [int(x) for x in input().split(", ")]
    # matrix.append(current_row)
    totol_sum += sum(current_row)
print(totol_sum)