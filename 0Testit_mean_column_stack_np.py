from samwise import pb
import numpy as np
# calc the means of a column

costs = np.column_stack(([2, 1, 2, 1],
                        [4, 6, 5, 5]))

mean_costs = np.mean(costs[:, 1])  # Every row, 2nd column get the means - add then all up and divide by all

print(costs)
pb(mean_costs,"mean_costs")


