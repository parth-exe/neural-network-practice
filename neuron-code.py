input_list = [1, 2, 3, 2.5]
associated_weights = [0.2, 0.8, -0.5, 1]
bias = 2


output = (input_list[0] * associated_weights[0] + 
        input_list[1] * associated_weights[1] + 
        input_list[2] * associated_weights[2] +
        bias)
print(output)