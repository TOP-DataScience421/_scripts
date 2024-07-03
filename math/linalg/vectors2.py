from numpy import array
from numpy.linalg import norm


v = array([[1, 2, 3, 7, 8, 9]])

# >>> v.shape
# (1, 6)

# >>> norm(v)
# np.float64(14.422205101855956)

# >>> sum(n**2 for n in v[0])**0.5
# np.float64(14.422205101855956)

# >>> norm(v.T)
# np.float64(14.422205101855956)


v_unit = v * 1/norm(v)

# >>> v_unit
# array([[0.06933752, 0.13867505, 0.20801257, 0.48536267, 0.5547002, 0.62403772]])

# >>> norm(v_unit)
# np.float64(1.0)


