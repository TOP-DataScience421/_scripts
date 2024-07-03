from numpy import array


m1 = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])

# >>> print(m1)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# >>> type(m1)
# <class 'numpy.ndarray'>
# >>>
# >>> m1.shape
# (4, 3)

for row in m1:
    for n in row:
        print(n, end=' ')

# >>> m1[3][2]
# np.int64(12)
# >>>
# >>> m1[3,2]
# np.int64(12)
# >>>
# >>> m1[-1,-1]
# np.int64(12)

# >>> m1[0]
# array([1, 2, 3])
# >>> m1[1]
# array([4, 5, 6])
# >>> m1[2]
# array([7, 8, 9])
# >>> m1[3]
# array([10, 11, 12])

# >>> m1[:,1]
# array([ 2,  5,  8, 11])

# >>> m1[2:,1]
# array([ 8, 11])
# >>>
# >>> m1[2:,1:]
# array([[ 8,  9],
#        [11, 12]])

# >>> m1[::2,::2]
# array([[1, 3],
#        [7, 9]])


# >>> m1.diagonal()
# array([1, 5, 9])
# >>>
# >>> array([m1[i][-i-1] for i in range(3)])
# array([3, 5, 7])

