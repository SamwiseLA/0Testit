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

l_nums = []
s_input = "1"
while s_input not in ["0", ""]  :
    s_input = input("please give numbers to average (0/spc-ends): ")
    if s_input not in ["0", ""]: l_nums.append(float(s_input))

f_tot = 0
if len(l_nums) > 0:
    for f_num in l_nums: f_tot = f_tot + f_num

    print(f"\n\n{l_nums}\n\nThe Average of {f_tot} / {len(l_nums)} = {f_tot / len(l_nums)}")

