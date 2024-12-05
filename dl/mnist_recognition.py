from keras.utils import to_categorical

from numpy import array
from PIL import Image

from pathlib import Path
from sys import path

import mnist


dir_path = Path(path[0]) / 'test/28'
images = [
    Image.open(img_path)
    for img_path in dir_path.iterdir()
]

digits_imgs_2 = [[[0]*28 for _ in range(28)] for _ in range(len(images))]

for i in range(len(images)):
    for y in range(28):
        for x in range(28):
            r, g, b, _ = images[i].load()[x,y]
            lum = (r + g + b) / 3
            digits_imgs_2[i][y][x] = round(lum)

digits_imgs_2 = array(digits_imgs_2)

x_test_2 = digits_imgs_2.reshape(len(images), 784)
x_test_2 = x_test_2 / 255

y_test_2 = array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 4, 8])
y_test_2 = to_categorical(y_test_2, 10)


print('\n РАСПОЗНАВАНИЕ \n')
results = mnist.model.predict(
    x_test_2, 
    verbose=2
)
# >>> results.round(2)
# array([[0.07, 0.  , 0.02, 0.  , 0.  , 0.  , 0.32, 0.  , 0.59, 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.66, 0.  , 0.  , 0.  , 0.01, 0.32, 0.  , 0.01, 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 1.  , 0.  ],
#        [0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.99, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.02, 0.09, 0.01, 0.  , 0.01, 0.  , 0.52, 0.34, 0.01],
#        [0.  , 0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.  , 0.01, 0.  , 0.  , 0.  , 0.  , 0.  , 0.99, 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 1.  , 0.  ]],
#       dtype=float32)

scores_2 = mnist.model.evaluate(
    x_test_2,
    y_test_2,
    verbose=2,
    return_dict=True,
)

print(
    '\nЗначение функции потерь: {loss:.3}\n'
    'Доля корректных распознаваний: {accuracy:.1%}'
    .format(**scores_2)
)

# Значение функции потерь: 2.04
# Доля корректных распознаваний: 69.2%

