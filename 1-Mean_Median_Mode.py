""" The mean is the average of all the integers in a set of values.
The median is the midpoint value of a data set for which an equal number of samples are less than and greater than the value.
For an odd sample size, this is the middle element of the sorted sample; for an even sample size, this is the average of the two middle elements of the sorted sample.
The mode is the element(s) that occurs most frequently in a data set. A set is multimodal if no number in the set appears more than one time, so every number in the set is a valid mode.
"""

import numpy as np
from scipy import stats

numbers = (64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060)

print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))


""" If the array contains more than one modal value, we choose the numerically smallest one.
"""

""" Given a discrete set of numbers, X, and a corresponding set of weights, W, the weighted mean is calculated as follows
"""

'$ m_{w} = \frac{\sum^{n}_{i=1}(x_{i}\times w_{i})}{\sum^{n}_{i=1}w_{i}} $'


# In Python

def weighted_mean(X, W):
    numerator = sum(a*b for a,b in zip(X,W))
    denominator = sum(W)
    return(round((numerator / denominator), 1))

X = [10, 40, 30, 50, 20]
W = [1, 2, 3, 4, 5]

print(weighted_mean(X, W))

# Output: 32.0
