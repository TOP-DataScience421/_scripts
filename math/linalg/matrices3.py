from numpy import dot
from numpy.random import default_rng


m1 = default_rng().integers(0, 10, (2, 4))
m2 = default_rng().integers(0, 10, (4, 3))

>>> m1
array([[2, 1, 2, 6],
       [9, 9, 2, 7]])
>>>
>>> m2
array([[9, 6, 3],
       [9, 3, 0],
       [9, 1, 5],
       [0, 1, 0]])


# >>> m1 @ m2
# array([[ 45,  23,  16],
#        [180,  90,  37]])
# >>>
# >>> dot(m1, m2)
# array([[ 45,  23,  16],
#        [180,  90,  37]])


# >>> dot(m1[0], m2[:,0])
# np.int64(45)
# >>>
# >>> dot(m1[0], m2[:,1])
# np.int64(23)
# >>>
# >>> dot(m1[0], m2[:,2])
# np.int64(16)
# >>>
# >>> dot(m1[1], m2[:,0])
# np.int64(180)
# >>>
# >>> dot(m1[1], m2[:,1])
# np.int64(90)
# >>>
# >>> dot(m1[1], m2[:,2])
# np.int64(37)

