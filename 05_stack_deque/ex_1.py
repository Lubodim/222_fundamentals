# 1, 2, 3, 4, 5, 6, 7, 8, 9
#6
# print(*input().split(", ")[::-1])


#5
# text = [int(t) for t in input().split(', ')]
# print(' '.join(str(t) for t in text[::-1]))

#4
# txt = input().split(', ')
# text = [int(t) for t in txt[::-1] if int(t) % 2 == 0]
# print(*text)


# 3
# text = list(map(int, input().split(', ')))
# print(*text[::-1])



#2
# text = input().split(", ")
# for _ in range(len(text)):
#     print(text.pop(), end=" ")

#1
# text = input().split(", ")
# print(text)
# len_test = len(text)
# for _ in range(len_test):
#     print(text.pop(), end=" ")