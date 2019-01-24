""" Use the fit function in the _sklearn.linear_model.LinearRegression_ class.
"""


from sklearn import linear_model
import numpy as np

xl = [1, 2, 3, 4, 5]
x = np.asarray(xl).reshape(-1, 1)
y = [2, 1, 4, 3, 5]
lm = linear_model.LinearRegression()
lm.fit(x, y)
print(lm.intercept_) # 0.6
print(lm.coef_[0]) # 0.8


""" Question:
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y,
can be expressed as the following list of (x,y) points:
(95,85), (85,95), (80,70), (70,65), (60,70)
If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method,
then compute and print the value of y when x=80.
"""

n = 5
X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]
b = (n*sum([X[i]*Y[i] for i in range(n)]) - sum(X)*sum(Y)) / (n*sum([X[i]**2 for i in range(n)]) - sum(X)**2)
a = sum(Y)/n - b*(sum(X)/n)
print(round(a+b*80, 3)) # y = 78.288
