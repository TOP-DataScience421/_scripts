from numpy import array
from numpy.linalg import norm
from scipy.linalg import null_space


m1 = array([[1, -1], [-2, 2]])
m2 = array([1, -1, -2, 3]).reshape(2, 2)
m3 = array([
    [3, 0],
    [5, 2],
    [1, 2],
])

# >>> null_space(m1)
# array([[0.70710678],
#        [0.70710678]])
# >>>
# >>> null_space(m2)
# array([], shape=(2, 0), dtype=float64)
# >>>
# >>> null_space(m3)
# array([], shape=(2, 0), dtype=float64)


# >>> norm(null_space(m1))
# np.float64(0.9999999999999999)


# >>> m3.T
# array([[3, 5, 1],
#        [0, 2, 2]])
# >>>
# >>> null_space(m3.T)
# array([[ 0.68599434],
#        [-0.51449576],
#        [ 0.51449576]])

