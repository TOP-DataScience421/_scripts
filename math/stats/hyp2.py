from matplotlib import pyplot as plt
from numpy import set_printoptions
from numpy import array, sort, exp, pi, average
from numpy.random import default_rng

set_printoptions(suppress=True)


def gauss(x, mean, std):
    return exp(-(x - mean)**2/(2*std**2)) / (std * (2*pi)**0.5)


n = 60

# X = default_rng().normal(10, 5, n)
X = array([2.02795313, 13.79460175, 6.82291532, 11.46817649, 10.61116166, 14.11485251, 12.85318865, 10.28921936, 4.05263727, 17.43211059, 10.90679277, 11.21807868, 7.11043682, 15.41674263, 10.47488197, 12.17116593, 5.17875048, 15.10017749, 11.45807574, 10.50367542, 9.76876195, 11.9698423, 5.93013584, 7.26378688, 18.50956957, 7.98948105, 7.43287705, 10.22612032, 7.26486096, 10.90339048, 8.85354952, 13.30993915, 7.64468885, 15.16482546, 8.67745351, 9.39069153, 11.90068156, 8.87239737, 6.6360926, 3.2695412, 10.55981307, 11.856502, 19.51660164, 10.74520819, 4.76488678, 8.10702425, 13.77657201, 4.25999383, 7.03433871, 7.82156803, 1.88893857, 7.60941887, 4.0073731, 8.90584472, 12.77543915, 6.17649869, 9.96733785, 9.22758886, 6.71636945, 11.20819275])

# plt.scatter(range(n), X)
# plt.show()

print(X.min(), X.max(), sep='\n', end='\n\n')
# print(sort(X))

X_intervals = {
    (0,4): 0,
    (4,8): 0,
    (8,12): 0,
    (12,16): 0,
    (16,20): 0,
}
for x_i in X:
    for rng in X_intervals:
        l, r = rng
        if l <= x_i <= r:
            X_intervals[rng] += 1

print(X_intervals, end='\n\n')

m_intervals = array([*X_intervals.values()])
X_intervals_means = array([(l+r)/2 for l, r in X_intervals])

print(array([X_intervals_means, m_intervals]), end='\n\n')

X_mean_sample = average(X)
X_var_sample = sum((x_i - X_mean_sample)**2 for x_i in X) / n
X_std_sample = X_var_sample ** 0.5

print(
    X_mean_sample,
    X_std_sample,
    sep='\n', 
    end='\n\n'
)

p_intervals = gauss(X_intervals_means, X_mean_sample, X_std_sample)

print(array([X_intervals_means, m_intervals, p_intervals]), end='\n\n')

chi_observed = sum((m_intervals - n*p_intervals)**2 / n*p_intervals)
chi_critical = 5.991


if chi_observed < chi_critical:
    print('основная гипотеза принята')
else:
    print('основная гипотеза отвергнута')

