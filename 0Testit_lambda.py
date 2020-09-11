# lambda -
# a single line function that takes 1 or more arguments
# and does a single line expression returning a value
# can be called within another function

from samwise import pb


def my_func(n):
    return lambda a, b: (a + b) * n


def my_func_add(n):
    return lambda a, b: (a + b) + n


f_g = lambda x, y, z: (x + y + z) * 5

a = f_g(2, 3, 4)

pb(a)

my_doubler = my_func(2)
my_tripler = my_func(3)
add_um_plus3 = my_func_add(3)

pb("5 & 100", "input")
pb(my_doubler(5, 100), "+*2")
pb(my_tripler(5, 100), "+*3")
pb(add_um_plus3(5, 100), "++3")
