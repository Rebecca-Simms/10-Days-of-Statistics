""" Question:
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
"""


N = 10
X = (10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2)
Y = (200, 44, 32, 24, 22, 17, 15, 12, 8, 4)

mux = sum(X) / N
muy = sum(Y) / N

stand_dev_x = (sum([(i - mux)**2 for i in X]) / N)**0.5
stand_dev_y = (sum([(i - muy)**2 for i in Y]) / N)**0.5

covariance = sum([(X[i] - mux) * (Y[i] - muy) for i in range(N)])

Pearson = covariance / (stand_dev_x * stand_dev_y * N)

print(round(Pearson, 3)) # 0.612


"""Question:
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
"""

def get_rank(X, N):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]

N = 10
X = (10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2)
Y = (200, 44, 32, 24, 22, 17, 15, 12, 8, 4)


rx = get_rank(X, N)
ry = get_rank(Y, N)

d = [(rx[i] -ry[i])**2 for i in range(N)]
spearman = 1 - (6 * sum(d)) / (N * (N*N - 1))

print(round(spearman, 3)) # 0.903
