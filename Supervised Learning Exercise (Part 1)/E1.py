import random

# AND
training_inputs = [[-1, -1],
                   [-1, 1],
                   [1, -1],
                   [1, 1]]

training_outputs = [-1, -1, -1, 1]
alfa = 0.05


def train(t_inputs, t_outputs):
    alfa = 0.05
    weights = [random.random() for i in range(len(t_inputs[0]) + 1)]
    delta_w = [0 for i in range(len(weights))]
    iterations = 0
    error = True
    while error:
        error = epoch(t_inputs, t_outputs, weights, delta_w, alfa)
        iterations = iterations + 1
    print(iterations)
    return iterations


def epoch(t_inputs, t_outputs, w, d_w, a):
    outputs = []
    for i in range(len(t_inputs)):
        output = w[0] + t_inputs[i][0] * w[1] + t_inputs[i][1] * w[2]
        if output > 0:
            output = 1
        else:
            output = -1
        error = t_outputs[i] - output
        for j in range(len(d_w)):
            if j == 0:
                d_w[j] = d_w[j] + a * error
            else:
                d_w[j] = d_w[j] + a * t_inputs[i][j - 1] * error
        outputs.append(output)
    for i in range(len(w)):
        w[i] = w[i] + d_w[i]

    return not training_outputs == outputs


'''runs = []

for i in range(30):
    runs.append(train(training_inputs, training_outputs))
print('Average: ', sum(runs) / 30)
print('Max epochs: ', max(runs), '- Min epochs ', min(runs))'''
