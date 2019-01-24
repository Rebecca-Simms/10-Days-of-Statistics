""" Question:
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
"""

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def binomial(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

b = 109
g = 100

result = round(sum([binomial(i, 6, b / (b+g)) for i in range(3, 7)]), 3)

print(result)
