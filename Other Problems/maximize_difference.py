"""
Find the maximum difference between any two numbers in an array.
"""

import numpy as np
import random

test_list = random.sample(range(1,100000),1000)

def max_diff(x):
    if len(x) <= 1:
        return "No solution for empty or single element list!!!"
    c_max = x[1] - x[0]
    max_i = None
    min_i = 0
    for i in range(1, len(x)):
        d = x[i] - x[min_i] 

        #change the minimum value if current is less than previous minimum value
        if x[i] <= x[min_i]:
            min_i = i

        #update maximum value if current difference is greater than previous max
        if d > c_max:
            c_max = d
            max_i = i

    return c_max, max_i, min_i

print(max_diff(test_list))

