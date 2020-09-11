from samwise import pb
import numpy as np
x = np.array([14, 21, 24, 7, 99])
y = np.array([12, 6, 23, 29, 77])  # a list of 5 items
z = np.array([x, y])  # each item is a row with a value of list, so 2 dimensional arrays.
pb(z.shape,"Show the shape for the numpy array (rows, cols): z.shape")
pb("","Array z")
print(z)


pb("","Array arr")
arr = np.array([[1, 2, 3, 4, 5],
                [11, 12, 13, 14, 15]
                ])

print(arr)
pb("","first row [0]")
print(arr[0])
pb("","first row [0], 2nd & 3rd item [1:3]")
print(arr[0][1:3])

z = np.array([
    [1, 2, 3, 4, 5, 55],
    [6, 7, 8, 9, 10, 100],
    [11, 12, 13, 14, 15, 150],
    [16, 17, 18, 19, 20, 200],
    [21, 22, 23, 24, 25, 250]
])

pb(""," numpy array")
print(z)
pb(""," numpy array from row 1:4(-1) get columns 1:5(-1)")
# returns a section of a 2 dim array,
# starting with 2nd row, ending with 4th row [1:4] and
# staring with 3nd column, ending with 5th column [2:5]
zz = z[1:4,2:5]
print(zz)

store = np.array(["X", "Z", "Z", "Z"])
cost = np.array([7, 1, 9, 4])
check_store = "Z"
# Check each value in corresponding list,
# and if there is a match, return the result
select_cost = cost[store == check_store]
print(select_cost)
pb(select_cost,f"Cost at store {check_store}")

stores = np.array([
    ["X", "Z", "Z", "Z"],
    [7, 1, 9, 4]
])
check_stores = "Z"
# Check each value in corresponding list,
# and if there is a match, return the result
#
# ONLY issue with using 2dim numpy is the have to be all the same datatype...
# this example changes thes numbers to string.
pb()
a = stores[0:1]
b = stores[1:]
select_costs = stores[1:][stores[0:1] == check_stores]
print(select_costs)
pb(select_costs,f"Cost at stores {check_stores}")