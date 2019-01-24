""" The quartiles of an ordered data set are the three points that split the data set into four equal groups. The three quartiles are defined as follows:
- Q1: The first quartile is the middle number between the smallest number in a data set and its median.
- Q2: The second quartile is the median (50% percentile) of the data set.
- Q3: The third quartile is the middle number between a data set's median and its largest number.
"""

""" We will split the data into two halves, lower half and upper half:
- If there are an odd number of data points in the original ordered data set, do not include the median (the central value in the ordered list) in either half.
- If there are an even number of data points in the original ordered data set, split this data set exactly in half.
"""

""" The value of the first quartile is the median of the lower half and the value of the third quartile is the median of the upper half.
"""

from statistics import median


def quartiles(numbers):
    numbers.sort()
    no_numbers = len(numbers)
    if no_numbers % 2 != 0:
        first_half = numbers[:len(numbers)//2]
        second_half = numbers[len(numbers)//2 + 1:]
        q1 = median(first_half)
        q3 = median(second_half)
        q2 = median(numbers)
    elif no_numbers % 2 == 0:
        first_half = numbers[:len(numbers)//2]
        second_half = numbers[len(numbers)//2:]
        q1 = median(first_half)
        q3 = median(second_half)
        q2 = median(numbers)
    return q1, q2, q3


numbers = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
print(quartiles(numbers)) # (15,40,43)


""" The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q1 - Q3).
"""


""" The expected value of a discrete random variable, X, is more or less another way of referring to the mean. The variance is the average magnitude of fluctuations of X from its expected value.
Given a data set, X, of size n, the variance can be calculated using
"""

'$\sigma^{2} = \frac{\sum^{n}_{i=1} (x_{i}-\mu)^{2}}{n}$'

""" The standard deviation quantifies the amount of variation in a set of data values and is given by the square root of the variance.
"""


def stand_dev(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum([((x - mean) ** 2) for x in X]) / len(numbers)
    standard_deviation = variance ** 0.5
    return round(standard_deviation, 1)

X = [10,40,30,50,20]

print(stand_dev(X)) # 14.1
