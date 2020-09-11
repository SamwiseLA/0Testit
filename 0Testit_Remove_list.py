from samwise import pb
# remove value from list

x = [9, 2, 4, 7, 8]
print(x)
pb(x, "Original x")

pb()

x.remove(9)
print(x)
pb(x, "Removed x")


