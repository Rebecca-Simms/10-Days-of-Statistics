""" Question:
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of ![equation](https://latex.codecogs.com/gif.latex?%5Cmu%3D205) pounds and a standard deviation of ![equation](https://latex.codecogs.com/gif.latex?%5Csigma%20%3D%2015) pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""

# First, note that

'$ \mu\' = n \times \mu = 49 \times 205 \ \ \ \ \text{and} \ \ \ \ \sigma\' = \sqrt{n}\times \sigma = 7 \times 15 $'

# Then, putting this into the Normal distribution probability function

import math

def cum_def(x, mean, stand_dev):
  p = 0.5 * (1 + math.erf((x - mean)/ (stand_dev * math.sqrt(2))))
  return p

result = round(cum_def(9800, 49*205, 15*7),4)

print(result)


""" Question:
 The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of
 mu=24 and a standard deviation of sigma=2.0

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""



n = 100
mean = 2.4
stand_dev = 2.0

result = round(cum_def(250, 100*2.4, 10*2.0),4)
print(result)

""" Question:
You have a sample of 100 values from a population with mean mu=500 and with standard deviation sigma=80. Compute the interval that covers the middle 95% of the distribution of the sample mean;
in other words, compute A and B such that P(A<x<B). Use the value of z=1.96. Note that z is the z-score.
"""


zScore = 1.96
stand_dev = 80
n = 100
mean = 500

marginOfError = zScore * stand_dev / math.sqrt(n);

print(mean - marginOfError)
print(mean + marginOfError)
