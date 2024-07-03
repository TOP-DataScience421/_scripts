from numpy import array, rint
from numpy.linalg import matrix_rank, inv, solve

from fractions import Fraction as frac


# x + y = 4
# –x/2 + y = 2

# x = [[x], [y]]

A = array([
    [1, 1],
    [-0.5, 1],
])
b = array([4, 2]).reshape(2, 1)

#    Ax = b
# A¯¹Ax = A¯¹b
#    Ix = A¯¹b
#     x = A¯¹b

x, y = (inv(A) @ b).flat

print(f'{x = !s}\n{y = !s}')

# x = 1.3333333333333337
# y = 2.6666666666666665

# >>> print(f'x = {frac(x).limit_denominator(10)}\ny = {frac(y).limit_denominator(10)}')
# x = 4/3
# y = 8/3

# >>> solve(A, b)
# array([[1.33333333],
#        [2.66666667]])

