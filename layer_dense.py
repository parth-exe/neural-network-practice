import numpy as np
import nnfs
from nnfs.datasets import spiral_data
# nnfs.init()
np.random.seed(0)
X = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, N_inp, N_neurons):
        self.weights = 0.10 * np.random.randn(N_inp, N_neurons)
        self.biases = np.zeros((1, N_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


Layer_1 = Layer_Dense(4, 3)
Layer_2 = Layer_Dense(3,2)

print("Layer 1")
Layer_1.forward(X)
print(Layer_1.output)
print("-"*15)
print("Layer 2")
Layer_2.forward(Layer_1.output)
print(Layer_2.output)

"""
Implementation using NNFS spiral dataset which plots points on a 2D plane returning X = Nx2 matrix and y = matrix containing values till class_value-1.
```
# X, y = spiral_data(samples=100, classes=3)
# dense = Layer_Dense(2,3)
# dense.forward(X)
# print(dense.output[-6:-1])
```

"""
