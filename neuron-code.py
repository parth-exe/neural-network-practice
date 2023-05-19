input_list = [1, 2, 3, 2.5]
associated_weights1 = [0.2, 0.8, -0.5, 1]
associated_weights2 = [0.5, -0.91, 0.26, -0.5]
associated_weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5


output = [
        # Neuron 1
        (input_list[0] * associated_weights1[0] + 
        input_list[1] * associated_weights1[1] + 
        input_list[2] * associated_weights1[2] +
        input_list[3] * associated_weights1[3] +
        bias1),
        # Neuron 2
        (input_list[0] * associated_weights2[0] + 
        input_list[1] * associated_weights2[1] + 
        input_list[2] * associated_weights2[2] +
        input_list[3] * associated_weights2[3] +
        bias2),
        # Neuron 3
        (input_list[0] * associated_weights3[0] + 
        input_list[1] * associated_weights3[1] + 
        input_list[2] * associated_weights3[2] +
        input_list[3] * associated_weights3[3] +
        bias3)
        ]
print(output)