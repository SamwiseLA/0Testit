from samwise import pb
import numpy as np
# calc the means of a column

y = np.array([4, 5, 6, 8])
x = np.array([19, 20, 21, 22])

y = np.corrcoef(x, y)

print(y)
print(y[1,0])

