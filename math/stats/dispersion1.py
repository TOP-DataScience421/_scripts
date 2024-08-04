from numpy import array, dot, var as np_var
from scipy.ndimage import variance as sp_var, standard_deviation as sp_std

from statistics import variance


X = array([-0.1, 0.2])
P1 = array([2/3, 1/3])
M_X = dot(X, P1)
D_X = sum((X[i] - M_X)**2 * P1[i] for i in range(len(X)))

# >>> array([X, P1])
# array([[-0.1       ,  0.2       ],
#        [ 0.66666667,  0.33333333]])
# >>>
# >>> M_X
# np.float64(0.0)
# >>>
# >>> D_X
# np.float64(0.020000000000000004)
# >>>
# >>> D_X**0.5
# np.float64(0.14142135623730953)


Y = array([-100, 100])
P2 = array([0.5, 0.5])
M_Y = dot(Y, P2)
D_Y = sum((Y[i] - M_Y)**2 * P2[i] for i in range(len(Y)))

# >>> array([Y, P2])
# array([[-100. ,  100. ],
#        [   0.5,    0.5]])
# >>>
# >>> M_Y
# np.float64(0.0)
# >>>
# >>> D_Y
# np.float64(10000.0)
# >>>
# >>> D_Y**0.5
# np.float64(100.0)


T1 = (X - M_X) / D_X**0.5

# >>> T1
# array([-0.70710678,  1.41421356])
# >>>
# >>> dot(T1, P1)
# np.float64(0.0)
# >>>
# >>> sum(T1[i]**2 * P1[i] for i in range(len(T1)))
# np.float64(0.9999999999999998)

T2 = (Y - M_Y) / D_Y**0.5

# >>> T2
# array([-1.,  1.])
# >>>
# >>> dot(T2, P2)
# np.float64(0.0)
# >>>
# >>> sum(T2[i]**2 * P2[i] for i in range(len(T2)))
# np.float64(1.0)

