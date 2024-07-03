from numpy import eye, concat, array
from numpy.random import default_rng
from sympy import Matrix


n = 2
A = default_rng().random((n,n))
I = eye(n)

A_I = concat([A, I], axis=1)
A_I_rref = array(
    Matrix(A_I).rref()[0],
    dtype=float
)
A_inv = A_I_rref[:,2:]


# >>> A
# array([[0.90065273, 0.58798007],
#        [0.9715792 , 0.84448613]])
# >>>
# >>> A_I
# array([[0.90065273, 0.58798007, 1.        , 0.        ],
#        [0.9715792 , 0.84448613, 0.        , 1.        ]])
# >>> 
# >>> A_inv
# array([[ 4.46063933, -3.10575501],
#        [-5.13195447,  4.7573155 ]])
# >>> 
# >>>
# >>> A_inv @ A
# array([[ 1.0000000e+00, -4.4408921e-16],
#        [-8.8817842e-16,  1.0000000e+00]])

