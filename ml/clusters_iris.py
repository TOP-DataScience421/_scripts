from matplotlib import pyplot as plt
from numpy import array
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


fig = plt.figure(figsize=(20, 12), layout='tight')
axs = fig.subplots(2, 6)


raw = load_iris()

data = DataFrame(raw['data'], columns=raw['feature_names'])
data_norm = (data - data.mean()) / data.std()


model = KMeans(3, n_init=10, random_state=15)
y_pred = model.fit_predict(data)

y_pred = array([
    1 if v == 0 else (0 if v == 1 else v)
    for v in y_pred
])

results = DataFrame(
    array([raw['target'], y_pred]).T,
    columns=['разметка', 'модель']
)
results['правильно'] = (raw['target'] == y_pred)
print(results['правильно'].value_counts(normalize=True).round(2))


axs[0][0].scatter(data.iloc[:, 0], data.iloc[:, 1], c=raw['target'], cmap='Paired')
axs[1][0].scatter(data.iloc[:, 0], data.iloc[:, 1], c=y_pred, cmap='Paired')

axs[0][1].scatter(data.iloc[:, 0], data.iloc[:, 2], c=raw['target'], cmap='Paired')
axs[1][1].scatter(data.iloc[:, 0], data.iloc[:, 2], c=y_pred, cmap='Paired')

axs[0][2].scatter(data.iloc[:, 0], data.iloc[:, 3], c=raw['target'], cmap='Paired')
axs[1][2].scatter(data.iloc[:, 0], data.iloc[:, 3], c=y_pred, cmap='Paired')

axs[0][3].scatter(data.iloc[:, 1], data.iloc[:, 2], c=raw['target'], cmap='Paired')
axs[1][3].scatter(data.iloc[:, 1], data.iloc[:, 2], c=y_pred, cmap='Paired')

axs[0][4].scatter(data.iloc[:, 1], data.iloc[:, 3], c=raw['target'], cmap='Paired')
axs[1][4].scatter(data.iloc[:, 1], data.iloc[:, 3], c=y_pred, cmap='Paired')

axs[0][5].scatter(data.iloc[:, 2], data.iloc[:, 3], c=raw['target'], cmap='Paired')
axs[1][5].scatter(data.iloc[:, 2], data.iloc[:, 3], c=y_pred, cmap='Paired')

plt.show()
