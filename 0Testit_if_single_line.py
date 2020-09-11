# if single line
from samwise import pb
s_input = input("please give 2 numbers sepearted by a space: ")
n_space = s_input.index(" ")

n_1 = float(s_input[0:n_space])
n_2 = float(s_input[n_space:])
# print(f"{n_1}:{n_2}")
s_oper = "*"
if n_1 * n_2 > 1000: s_oper = "+"

# value set conditionally
n_val = n_1 * n_2 if n_1 * n_2 <= 1000 else n_1 + n_2

pb(f"{n_1} {s_oper}\n{n_2} =\n----------\n{n_val}","If product of numbers is <= 1000, add them")