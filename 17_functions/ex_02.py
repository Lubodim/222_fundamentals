from math import sqrt


def list_sqrt(numb):
    return list(map(sqrt, numb))


nums = list(map(int, input().split(", ")))
sqrts = list_sqrt(nums)

for i, num in enumerate(sqrts):
    print(f"Square of {nums[i]} = {num:.2f}")
