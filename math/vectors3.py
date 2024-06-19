from numpy import array, dot


v = array([1, 2, 3, 4])
w = array([5, 6, 7, 8])

# >>> sum(v[i]*w[i] for i in range(len(v)))
# np.int64(70)

# >>> dot(v, w)
# np.int64(70)

# >>> v * 10
# array([10, 20, 30, 40])
# >>>
# >>> dot(v*10, w)
# np.int64(700)


a = array([0, 1, 2])
b = array([3, 5, 8])
c = array([13, 21, 24])

dot1 = dot(a, b+c)
dot2 = dot(a, b) + dot(a, c)

# >>> dot1 == dot2
# np.True_


v1 = array([0, 5])
v2 = array([5, 0])

# >>> dot(v1, v2) == 0
# np.True_


