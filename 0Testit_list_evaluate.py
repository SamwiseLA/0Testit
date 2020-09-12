from samwise import pb
# create list from criteria

l_i = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9]
pb("", "Original p")
print(l_i)

pb("", "Evaluate Numbers? and build a new list based on criteria")

l_y = [i for i in range(10) if i > 3]

print(l_y)

pb("", "Evaluate List and build a new list based on criteria")

l_z1 = [j for j in l_i if j >= 7]

print(l_z1)

pb("", "Evaluate List and build a new list by augmenting the list")

l_o = ['hello', 'world']

l_u = [u.upper().replace("O", "?") for u in l_o]
l_z2 = [j + 1 for j in l_i if j >= 7]

print(f"Orig:                           {l_o}")
print(f'upper() and changed "O" to "?": {l_u}')
print(f"Num List: {l_i}")
print(f"Num List Evaluated >= 7:               {l_z1}")
print(f"Num List Evaluated >= 7 & Altered + 1: {l_z2}")

pb(f"{l_u}", f'upper() and changed "O" to "? (w/ format)": {l_u}')
pb(l_u, f"upper() and changed \"O\" to \"?\" (no format): {l_u}")

l_h = [i * 3 for i in range(5)]  # 0 - 4, * 3, place value in list.
pb(f"{l_h}", "How to get output of: [0, 3, 6, 9, 12]")


#Find The Most Frequent Value In A List.
l_test = ["q", "s", "s", "q", "a", "q", "p", "t", "p", "a", "s", "t", "q", "q", "q", "t"]
l_sort = sorted(l_test, reverse=True)
pb(f"{l_sort}")

l_sort = sorted(l_test, key = l_test.count, reverse=True)
pb(f"{l_sort}")

d_test = {}
s_test = set(l_test)
for item in s_test:
    d_test[item] = l_test.count(item)

pb(d_test)

s_test = set(l_test)

pb(f"{l_test}", "Orig List")
pb(f"{s_test}", "Unique #'s")

n_most = max(s_test, key = l_test.count)

print(f"Most Frequent Item: {n_most}")

# Lambda -
# -
# use a variable BUT add parameters,
# have the set up of that variable =
# lambda & the number of parameters as new variables & :
# then create any single return equation with those variables
# and that will be the value of of the variable used
# -
pb()

test1 = lambda ab, cd: ab + (cd * 3)
test2 = lambda ab, cd: (ab + cd) * 3

pb(test1(5, 3), "test1(5, 3): test1 = lambda ab, cd: ab + (cd * 3)")
pb(test2(5, 3), "test2(5, 3): test2 = lambda ab, cd: (ab + cd) * 3")

pb("",)

orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}

lb_orders = {"A":5, "B":6, "C":7, "D":8, "E":9}
li_orders = lb_orders.items()

l_items = orders.items()

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)  # reverse order baseded on value x[1] in dict
best_selling = max(orders.items(), key=lambda x: x[1]) # max number sold in dict based on value x[1]
worst_selling = min(orders.items(), key=lambda x: x[1]) # min number sold in dict on value x[1]

pb([l_items, sort_orders], "Originl & Sorted List")


pb("","Sorted by number sold")
for i in sort_orders:
    print(i[0], i[1])

pb(best_selling[0],"Best Selling")
pb(worst_selling[0],"Worst Selling")