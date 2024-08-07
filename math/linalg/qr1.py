from numpy import dot, zeros, rint
from numpy.linalg import norm
from numpy.random import default_rng


n = 3
V = default_rng().integers(-9, 10, size=(n,n))
Q = zeros((n,n))


# >>> V
# array([[ 8,  5, -4],
#        [-1,  3,  5],
#        [ 1, -8,  3]])
# >>>
# >>> Q
# array([[0., 0., 0.],
#        [0., 0., 0.],
#        [0., 0., 0.]])

# пошагово:

# шаг 1
# >>> k = 0
# >>>
# >>> Q[:,k] = V[:,k]
# >>> Q
# array([[ 8.,  0.,  0.],
#        [-1.,  0.,  0.],
#        [ 1.,  0.,  0.]])
# >>>
# >>> Q[:,k] = Q[:,k] / norm(Q[:,k])
# >>> Q
# array([[ 0.98473193,  0.        ,  0.        ],
#        [-0.12309149,  0.        ,  0.        ],
#        [ 0.12309149,  0.        ,  0.        ]])

# шаг 2
# >>> k = 1
# >>>
# >>> Q[:,k] = V[:,k]
# >>> Q
# array([[ 0.98473193,  5.        ,  0.        ],
#        [-0.12309149,  3.        ,  0.        ],
#        [ 0.12309149, -8.        ,  0.        ]])
# >>>
# >>> Q[:,k] = Q[:,k] - dot(Q[:,k], Q[:,0]) * Q[:,0]
# >>> Q
# array([[ 0.98473193,  1.48484848,  0.        ],
#        [-0.12309149,  3.43939394,  0.        ],
#        [ 0.12309149, -8.43939394,  0.        ]])
# >>>
# >>> Q[:,k] = Q[:,k] / norm(Q[:,k])
# >>> Q
# array([[ 0.98473193,  0.16081096,  0.        ],
#        [-0.12309149,  0.3724907 ,  0.        ],
#        [ 0.12309149, -0.913997  ,  0.        ]])

# шаг 3
# >>> k = 2
# >>>
# >>> Q[:,k] = V[:,k]
# >>> Q
# array([[ 0.98473193,  0.16081096, -4.        ],
#        [-0.12309149,  0.3724907 ,  5.        ],
#        [ 0.12309149, -0.913997  ,  3.        ]])
# >>>
# >>> Q[:,k] = Q[:,k] - dot(Q[:,k], Q[:,0]) * Q[:,0] - dot(Q[:,k], Q[:,1]) * Q[:,1]
# >>> Q
# array([[ 0.98473193,  0.16081096,  0.36609206],
#        [-0.12309149,  0.3724907 ,  5.05207037],
#        [ 0.12309149, -0.913997  ,  2.12333393]])
# >>>
# >>> Q[:,k] = Q[:,k] / norm(Q[:,k])
# >>> Q
# array([[ 0.98473193,  0.16081096,  0.06665482],
#        [-0.12309149,  0.3724907 ,  0.91983649],
#        [ 0.12309149, -0.913997  ,  0.38659794]])

# проверка
# >>> Q.T @ Q
# array([[ 1.00000000e+00,  4.16333634e-17, -6.93889390e-18],
#        [ 4.16333634e-17,  1.00000000e+00,  5.55111512e-17],
#        [-6.93889390e-18,  5.55111512e-17,  1.00000000e+00]])
# >>>
# >>> rint(Q.T @ Q)
# array([[ 1.,  0., -0.],
#        [ 0.,  1.,  0.],
#        [-0.,  0.,  1.]])

