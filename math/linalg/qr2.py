from numpy import dot, zeros, round as np_round
from numpy.linalg import norm, qr
from numpy.random import default_rng


n = 3
A = default_rng().integers(-9, 10, size=(n,n))
Q = zeros((n,n))

for k in range(n):
    # целевой вектор
    Q[:,k] = v_k = A[:,k]
    # ортогонализация
    for j in range(k):
        # опорный вектор
        q_j = Q[:,j]
        Q[:,k] -= dot(v_k, q_j) * q_j
    # нормализация
    Q[:,k] /= norm(Q[:,k])


# >>> A
# array([[ 1,  1, -1],
#        [-1,  4, -5],
#        [-1, -3,  7]])
# >>>
# >>> Q
# array([[ 0.57735027,  0.19611614,  0.79259392],
#        [-0.57735027,  0.78446454,  0.22645541],
#        [-0.57735027, -0.58834841,  0.56613852]])
# >>>
# >>> Q.T @ Q
# array([[1.00000000e+00, 0.00000000e+00, 1.11022302e-16],
#        [0.00000000e+00, 1.00000000e+00, 2.22044605e-16],
#        [1.11022302e-16, 2.22044605e-16, 1.00000000e+00]])
# >>>
# >>> np_round(Q.T @ Q)
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
# >>>
# >>> R = Q.T @ A
# >>> R
# array([[ 1.73205081e+00,  0.00000000e+00, -1.73205081e+00],
#        [ 0.00000000e+00,  5.09901951e+00, -8.23687768e+00],
#        [ 2.22044605e-16,  1.11022302e-15,  2.03809866e+00]])
# >>>
# >>> np_round(R, 8)
# array([[ 1.73205081,  0.        , -1.73205081],
#        [ 0.        ,  5.09901951, -8.23687768],
#        [ 0.        ,  0.        ,  2.03809866]])
# >>>
# >>> Q @ R
# array([[ 1.,  1., -1.],
#        [-1.,  4., -5.],
#        [-1., -3.,  7.]])
# >>>
# >>> np_round(Q @ R) == A
# array([[ True,  True,  True],
#        [ True,  True,  True],
#        [ True,  True,  True]])


Q_, R_ = qr(A)

# >>> Q_
# array([[-0.57735027, -0.19611614,  0.79259392],
#        [ 0.57735027, -0.78446454,  0.22645541],
#        [ 0.57735027,  0.58834841,  0.56613852]])
# >>> R_
# array([[-1.73205081,  0.        ,  1.73205081],
#        [ 0.        , -5.09901951,  8.23687768],
#        [ 0.        ,  0.        ,  2.03809866]])
# >>>
# >>> Q_ @ R_
# array([[ 1.,  1., -1.],
#        [-1.,  4., -5.],
#        [-1., -3.,  7.]])
# >>>
# >>> A
# array([[ 1,  1, -1],
#        [-1,  4, -5],
#        [-1, -3,  7]])
# >>>
# >>> np_round(Q @ R, 8) == np_round(Q_ @ R_, 8)
# array([[ True,  True,  True],
#        [ True,  True,  True],
#        [ True,  True,  True]])

