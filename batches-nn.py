import numpy as np
# from nnfs.datasets import spiral_data
# import nnfs
inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]
associated_weights = [[0.2, 0.8, -0.5, 1],
                      [0.5, -0.91, 0.26, -0.5],
                      [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
associated_weights2 = [[0.1, -0.14, 0.5],
                       [-0.5, 0.12, -0.33],
                       [-0.44, 0.73, -0.13]]
biases_2 = [-1, 2, -0.5]
# Layer 1
print("Layer 1")
layer1_output = np.dot(inputs, np.array(associated_weights).T) + biases
print(layer1_output)
# Layer 2
print("Layer 2")
layer2_output = np.dot(layer1_output, np.array(associated_weights2).T) + biases_2
print(layer2_output)