# Dictionary List Stuff
from samwise import pb

l_fruit = {
    'apple': 1,
    'banana': 2,
    'coconut': 3
}

pb(f"{l_fruit}", "Original")
l_fruit['pear'] = "x"

pb(f"{l_fruit}", "After adding an additional item")

pb(l_fruit["pear"], "get back value of pear")

l_fruit["pear"] = 40

pb(f"{l_fruit}", "After changing pear value")



