from numpy import array, dot
from numpy.linalg import norm


a = array([4, 8])
b = array([5, 2])

beta = dot(a, b) / dot(a, a)

# >>> beta
# np.float64(0.45)

# >>> beta*a
# array([1.8, 3.6])

# >>> b - beta*a
# array([ 3.2, -1.6])
# >>> 
# >>> norm(b - beta*a)
# np.float64(3.577708763999664)

# >>> dot(a, b-beta*a)
# np.float64(0.0)

t = array([4, 5])
r = array([10, 3])

t_coll = dot(t, r) / dot(r, r) * r
t_orth = t - t_coll

# >>> dot(t_coll, t_orth)
# np.float64(3.552713678800501e-15)

