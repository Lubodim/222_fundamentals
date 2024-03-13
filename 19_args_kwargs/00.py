def my_func(param1, param2, *args, **kwargs):
    print(f"{param1}\n{param2}\n{args}\n{kwargs}")

def my_simple(**kwargs):
    print(kwargs)
my_func(1, 2, 2, 3,4 ,5, 4, 5, 1, name="Spiridon", email="spiridon@gmail.com", age=30)

my_simple(name="Spiridon", email="spiridon@gmail.com", age=30)

# def my_func(f_name, l_name, email, *args):
#     print(f"{f_name} {l_name} have {args} grades")
#
#
# my_func("Spiridon","Ivanov", "spiridon@gmail.com",2, 3, 4, 5, 6, 3, 5)