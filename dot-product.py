import numpy as np

inputs = [1, 2, 3, 2.5]
associated_weights = [[0.2, 0.8, -0.5, 1],
                      [0.5, -0.91, 0.26, -0.5],
                      [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

output_layer = []
"""
[!] Method to find output layer without using numpy dot product. [!]
```for neuron_weight, neuron_bias in zip(associated_weights, biases):
    neuron_output = 0
    for inp, weight in zip(inputs, neuron_weight):
        neuron_output += inp*weight
    neuron_output += neuron_bias
    output_layer.append(neuron_output)```
"""
output_layer = np.dot(associated_weights, inputs) + biases

print(output_layer)