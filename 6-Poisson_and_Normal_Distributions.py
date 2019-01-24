""" Question:
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
What is the probability that a car can be assembled at this plant in:
a) Less than 19.5 hours?
"""


from math import *

stand_dev=2

def cum_def(x,mu):
    erf_ = erf((x - mu) / (stand_dev*sqrt(2)))
    p = (1 + erf_) / 2
    return p

print(round(cum_def(19.5,20),3))


""" b) Between 20 and 22 hours?
"""

print(round(cum_def(22,20)-cum_def(20,20),3))


""" Question:
The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. If we can approximate the distribution of these grades by a normal distribution,
what percentage of the students:
- Scored higher than 80?
- Passed the test grade > 60?
- Failed the test grade < 60
"""

from math import *

stand_dev = 10

def cum_def(x, mu):
    erf_ = erf((x - mu) / (stand_dev*sqrt(2)))
    p = (1 + erf_) / 2
    return p

result1 = (1 - cum_def(80, 70)) * 100
result2 = (1 - cum_def(60, 70)) * 100
result3 = cum_def(60, 70) * 100

print(round(result1, 2))
print(round(result2, 2))
print(round(result3, 2))
