from numpy import array, eye, diag
from numpy.linalg import matrix_rank
from numpy.random import default_rng
from scipy.linalg import null_space


m1 = default_rng().integers(0, 10, size=(2, 2))
# [[1 3]
#  [4 7]]

m2 = default_rng().integers(0, 10, size=(3, 3))
# [[7 5 4]
#  [9 8 2]
#  [9 7 8]]

m3 = array([
    [1, 2, 4],
    [2, 4, 8],
    [3, 6, 12],
])

m4 = diag(default_rng().integers(-5, 6, size=4))
# [[-2  0  0  0]
#  [ 0 -4  0  0]
#  [ 0  0 -4  0]
#  [ 0  0  0 -2]]


# >>> m1
# array([[1, 3],
#        [4, 7]])
# >>>
# >>> null_space(m1)
# array([], shape=(2, 0), dtype=float64)
# >>>
# >>> null_space(m1.T)
# array([], shape=(2, 0), dtype=float64)
# >>>
# >>> matrix_rank(m1)
# np.int64(2)


# >>> m2
# array([[7, 5, 4],
#        [9, 8, 2],
#        [9, 7, 8]])
# >>>
# >>> null_space(m2)
# array([], shape=(3, 0), dtype=float64)
# >>>
# >>> null_space(m2.T)
# array([], shape=(3, 0), dtype=float64)
# >>>
# >>> matrix_rank(m2)
# np.int64(3)


# >>> m3
# array([[ 1,  2,  4],
#        [ 2,  4,  8],
#        [ 3,  6, 12]])
# >>>
# >>> null_space(m3)
# array([[-0.97590007, -0.        ],
#        [ 0.09759001,  0.89442719],
#        [ 0.19518001, -0.4472136 ]])
# >>>
# >>> null_space(m3.T)
# array([[ 0.57735027,  0.77151675],
#        [ 0.57735027, -0.6172134 ],
#        [-0.57735027,  0.15430335]])
# >>>
# >>> matrix_rank(m3)
# np.int64(1)


# >>> m4
# array([[-2,  0,  0,  0],
#        [ 0, -4,  0,  0],
#        [ 0,  0, -4,  0],
#        [ 0,  0,  0, -2]])
# >>>
# >>> matrix_rank(m4)
# np.int64(4)
# >>>
# >>> m4[1,1] = 0
# >>> m4
# array([[-2,  0,  0,  0],
#        [ 0,  0,  0,  0],
#        [ 0,  0, -4,  0],
#        [ 0,  0,  0, -2]])
# >>>
# >>> matrix_rank(m4)
# np.int64(3)

