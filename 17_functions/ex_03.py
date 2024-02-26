
# def abs_nums(nums):
#     new_nums = []
#     for num in nums:
#         new_nums.append(abs(num))
#     return new_nums
# print(f"{abs_nums(numbs)}")

numbs = list(map(float, input().split(" ")))
abs_num = lambda x: abs(x)
abs_list = []
for num in numbs:
    curr_num = abs_num(num)
    abs_list.append(curr_num)
print(abs_list)






# print([abs(float(x)) for x in input().split()])