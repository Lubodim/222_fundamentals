# print(ord("A"))
#
# print(chr(97))
for ch in range(1, 55295 + 1):
    if ch % 50 == 0:
        print()
    print(chr(ch), end=', ')


