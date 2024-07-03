from numpy import array


x = array([
    (1,), 
    (4,), 
    (5,), 
    (6,),
])
y = array([[.5], [-7]])
z = array([[1, 4, 5, 6]])

# >>> type(x)
# <class 'numpy.ndarray'>

# ndarray — n-dimensional array — многомерный массив

# >>> x.shape
# (4, 1)
# >>> y.shape
# (2, 1)
# >>> z.shape
# (1, 4)

# >>> len(x)
# 4
# >>> len(y)
# 2
# >>> len(z)
# 1

# >>> x.T
# array([[1, 4, 5, 6]])
# >>>
# >>> y.T
# array([[ 0.5, -7. ]])
# >>>
# >>> z.T
# array([[1],
#        [4],
#        [5],
#        [6]])

# >>> x == x.T.T
# array([[ True],
#        [ True],
#        [ True],
#        [ True]])
# >>>
# >>> all(x == x.T.T)
# True


v1 = array([[4], [5], [6]])
v2 = array([[10], [20], [30]])

# >>> v1 + v2
# array([[14],
#        [25],
#        [36]])

# >>> v1 - v2
# array([[ -6],
#        [-15],
#        [-24]])

# >>> v1 + array([[10], [20], [30], [40]])
# ValueError: operands could not be broadcast together with shapes (3,1) (4,1)

# >>> v2.T
# array([[10, 20, 30]])
# >>>
# >>> v1 + v2.T
# array([[14, 24, 34],
#        [15, 25, 35],
#        [16, 26, 36]])

v = array([[1, 2, 3]]).T
# >>> v
# array([[1],
#        [2],
#        [3]])

w = array([[10, 20]])

# >>> res1 = v + w
# >>> res1
# array([[11, 21],
#        [12, 22],
#        [13, 23]])
# >>> res1.shape
# (3, 2)

# >>> res2 = v.T + w.T
# >>> res2
# array([[11, 12, 13],
#        [21, 22, 23]])
# >>> res2.shape
# (2, 3)


# >>> v + 5
# array([[6],
#        [7],
#        [8]])
# >>>
# >>> v - 5
# array([[-4],
#        [-3],
#        [-2]])
# >>> 
# >>> v * 10
# array([[10],
#        [20],
#        [30]])

