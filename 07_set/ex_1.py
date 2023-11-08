my_set = set(input() for _ in range(int(input())))
while my_set:
    print(my_set.pop())


# my_set = set()
# for _ in range(int(input)):
#     current_name = input() # my_set.add(input())
#     my_set.add(current_name)
#
# while my_set:
#     print(my_set.pop())





# number = int(input())
# unic_list = []
# for _ in range(number):
#     current_name = input()
#     unic_list.append(current_name)
#
# my_set = set(unic_list)
# print(my_set)
#
# while my_set:
#     print(my_set.pop())



# number = int(input())
# unic_list = []
# for _ in range(number):
#     current_name = input()
#     if current_name not in unic_list:
#         unic_list.append(current_name)
#
# while unic_list:
#     print(unic_list.pop())


# number = int(input())
# my_list = []
# unic_list = []
# for _ in range(number):
#     current_name = input()
#     my_list.append(current_name)
#
# for i in range(len(my_list)):
#     if my_list[i] not in unic_list:
#         unic_list.append(my_list[i])
#
# while unic_list:
#     print(unic_list.pop())