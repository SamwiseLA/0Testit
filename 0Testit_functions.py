# Define and use a class
from samwise import pb

# funcytion returns multiple items when returning

def f_x():
    return 1, "apple", 3, "cat"


# call to function that receives 4 return values,
# they can received as individual variables or as a list
a, b, c, d = f_x()
l_y = f_x()

print(a, b, c, d)
print(l_y)