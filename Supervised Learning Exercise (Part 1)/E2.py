from E1 import train
import random

# XOR
training_inputs = [[-1, -1],
                   [-1, 1],
                   [1, -1],
                   [1, 1]]
training_outputs = [-1, 1, 1, -1]


# DOES NOT LEARN
# Peceptron draws linear separation between classes, not
# suitable for all problems (XOR)
train(training_inputs, training_outputs)