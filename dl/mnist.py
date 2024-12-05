from keras.layers import Dense, Input
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical

from numpy import load as np_load
from matplotlib import pyplot as plt
from pathlib import Path
from sys import path


digits_imgs = np_load(Path(path[0]) / 'mnist.npz')

x_train = digits_imgs['x_train']
y_train = digits_imgs['y_train']
x_test = digits_imgs['x_test']
y_test = digits_imgs['y_test']

# >>> x_train.shape
# (60000, 28, 28)
# >>>
# >>> y_train.shape
# (60000,)
# >>>
# >>> x_test.shape
# (10000, 28, 28)
# >>>
# >>> y_test.shape
# (10000,)

# print(y_train[2])
# plt.imshow(x_train[2], cmap='gray')
# plt.show()


# понижение ранга тензора без потери данных
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# масштабирование данных
x_train = x_train / 255
x_test = x_test / 255

# one hot encoding
#   0 -> [1 0 0 0 0 0 0 0 0 0]
#   1 -> [0 1 0 0 0 0 0 0 0 0]
#   2 -> [0 0 1 0 0 0 0 0 0 0]
#   3 -> [0 0 0 1 0 0 0 0 0 0]
#   4 -> [0 0 0 0 1 0 0 0 0 0]
#   5 -> [0 0 0 0 0 1 0 0 0 0]
#   6 -> [0 0 0 0 0 0 1 0 0 0]
#   7 -> [0 0 0 0 0 0 0 1 0 0]
#   8 -> [0 0 0 0 0 0 0 0 1 0]
#   9 -> [0 0 0 0 0 0 0 0 0 1]
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# конструирование искусственной нейронной сети
model = Sequential(name='handwritten_digits_recognition')
model.add(Input(shape=(784,)))
model.add(Dense(units=400, activation='relu'))
model.add(Dense(units=200, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# >>> model.summary()
# Model: "handwritten_digits_recognition"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 400)                 │         314,000 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 200)                 │          80,200 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_2 (Dense)                      │ (None, 10)                  │           2,010 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 396,210 (1.51 MB)
#  Trainable params: 396,210 (1.51 MB)
#  Non-trainable params: 0 (0.00 B)

# конфигурирование искусственной нейронной сети
model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(),
    metrics=[
        CategoricalAccuracy(name='accuracy'),
    ],
)


epochs = 20

print('\n ОБУЧЕНИЕ \n')
# обучение (предварительное) искусственной нейронной сети
training_results = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=epochs,
    validation_split=0.1,
    verbose=2,
)

print('\n ТЕСТИРОВАНИЕ \n')
# оценка эффективности обучения
scores = model.evaluate(
    x_test,
    y_test,
    batch_size=128,
    verbose=2,
    return_dict=True,
)

fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(1, 2)

axs[0].plot(training_results.history['loss'], label='loss')
axs[0].plot(training_results.history['val_loss'], label='val_loss')
axs[0].scatter(epochs, scores['loss'], s=50, c='r', label='test_loss')
axs[0].legend()

axs[1].plot(training_results.history['accuracy'], label='accuracy')
axs[1].plot(training_results.history['val_accuracy'], label='val_accuracy')
axs[1].scatter(epochs, scores['accuracy'], s=50, c='r', label='test_accuracy')
axs[1].legend()

plt.show()

