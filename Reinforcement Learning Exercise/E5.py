import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seed

random.seed(125)


def reward(state):
    if state == 100:
        return 100
    else:
        return 0


'''
[LEFT,RIGHT,UP,DOWN]
[ 0  ,  1 , 2,  3  ]
'''


def choose_action(state, matrix):
    possible_actions = []
    if state % 10 == 1:
        possible_actions.append(1)
    elif state % 10 == 0:
        possible_actions.append(0)
    else:
        possible_actions.append(1)
        possible_actions.append(0)
    if state - 10 > 0: possible_actions.append(2)
    if state + 10 <= 100: possible_actions.append(3)
    possible_states_utility = []
    for i in possible_actions:
        possible_states_utility.append(matrix[state - 1][i])
    m = max(possible_states_utility)
    max_idx = [i for i, j in enumerate(possible_states_utility) if j == m]
    chosen_action = random.choice(max_idx)
    return possible_actions[chosen_action]


def state_transition(iterations, matrix):
    state = 1
    alfa = 0.9
    discount = 0.99
    next_state = 0
    steps = [100, 200, 500, 600, 700, 800, 900, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 19999]
    for i in range(iterations):

        if state == 100:
            action_reward = reward(state)
            matrix[state - 1][action] = (1 - alfa) * matrix[state - 1][action] + alfa * (action_reward + discount * 0)
            state = 1

        else:
            action = choose_action(state, matrix)
            if action == 0:
                next_state = state - 1
            elif action == 1:
                next_state = state + 1
            elif action == 2:
                next_state = state - 10
            elif action == 3:
                next_state = state + 10
            action_reward = reward(state)
            print(state, next_state)
            matrix[state - 1][action] = (1 - alfa) * matrix[state - 1][action] + alfa * (
                        action_reward + discount * max(matrix[next_state - 1]))
            state = next_state

    matrix2arr = []
    for j in range(len(matrix)):
        matrix2arr.append(max(matrix[j]))
    arr = np.asmatrix(np.split(np.array(matrix2arr), 10))
    sns.heatmap(arr)
    plt.show()

'''if i == 0:
    action = random.choice([0,2,3,1])
else:
    action = choose_action(state)'''


for k in range(30):

    env = [[random.random() for j in range(4)] for i in range(100)]
    state_transition(20000, env)
