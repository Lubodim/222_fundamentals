from os import path

if not path.exists("text.txt"):
    with open("text.txt", "w") as f:
        f.write("Something\n")
else:
    with open("text.txt", "w") as f:
        f.write("Something new\n")



# Задача 2
# with open("data.txt", "a") as d:
#     while True:
#         new_txt = input("Enter your text: ")
#         if new_txt == "end":
#             break
#         d.write(f"{new_txt}\n")
#
# with open("data.txt", "r") as d:
#     print(d.read())






# задача 1
# with open("output.txt", "w") as spiridon:
#     spiridon.write("Something new\n")
#
# with open("output.txt", "r") as outp:
#     print(outp.read())
