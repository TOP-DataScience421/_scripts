from numpy import array, dot, exp, pi


def gauss(x, mean, std):
    return exp(-(x - mean)**2 / (2 * std**2)) / (std * (2*pi)**.5)


h = 10
n = 200

x_interval = array([15, 25, 35, 45, 55])
m = array([12, 43, 79, 47, 19])
x_mean_sample = dot(m, x_interval) / n

# >>> x_mean_sample
# np.float64(35.9)

C = x_interval.mean()
x_interval_dev = (x_interval - C) / h

x_mean_interval = dot(m, x_interval_dev) / n
x_p2_mean_interval = dot(m, x_interval_dev**2) / n

std_sample = ((x_p2_mean_interval - x_mean_interval**2) * h**2)**.5

p = gauss(x_interval, x_mean_sample, std_sample) * h
m_empiric = (n * p).round()


chi_obs = sum((m - m_empiric)**2 / m_empiric)
chi_crit = 9.2


assert chi_obs < chi_crit

