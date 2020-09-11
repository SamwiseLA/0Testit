from samwise import pb
# del values from list

p = ["j", "x", "n", "k", "e", "x"]
pb("", "Original p")
print(p)

pb()

pb("", "del from p: del(p[3:5])")
del(p[3:5])
print(p)
