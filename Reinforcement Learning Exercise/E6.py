import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

matrix = [[round(random.uniform(-0.1, 1.0), 2) for j in range(4)] for i in range(100)]
print(matrix)
'''
[LEFT,RIGHT,UP,DOWN]
'''


def reward(state):
    if state == 100:
        return 100
    else:
        return 0


def choose_state_E5(state):
    possible_states = []
    greed = 0.1
    if state % 10 == 1:
        possible_states.append(1)
    elif state % 10 == 0:
        possible_states.append(0)
    else:
        possible_states.append(1)
        possible_states.append(0)
    if state - 10 > 0: possible_states.append(2)
    if state + 10 <= 100: possible_states.append(3)
    possible_states_utility = []
    for i in possible_states:
        possible_states_utility.append(matrix[state - 1][i])
    is_greedy_bastard = random.random()
    if is_greedy_bastard < greed:
        m = max(possible_states_utility)
        max_idx = [i for i, j in enumerate(possible_states_utility) if j == m]
        chosen_state = random.choice(max_idx)
        return possible_states[chosen_state]
    else:
        return random.choice(possible_states)


def state_transition_E5(iterations):
    state = 1
    alfa = 0.05
    discount = 0.9
    next_state = 0
    for i in range(iterations):
        action = choose_state_E5(state)
        if action == 0:
            next_state = state - 1
        elif action == 1:
            next_state = state + 1
        elif action == 2:
            next_state = state - 10
        elif action == 3:
            next_state = state + 10
        action_reward = reward(state)
        if state == 100:
            matrix[state - 1][action] = (1 - alfa) * matrix[state - 1][action] + alfa * (action_reward + discount * 0)
            state = 1
        else:
            matrix[state - 1][action] = (1 - alfa) * matrix[state - 1][action] + alfa * (
                        action_reward + discount * matrix[next_state - 1][action])
            state = next_state
    matrix2arr = []
    for i in range(len(matrix)):
        matrix2arr.append(max(matrix[i]))
    arr = np.asmatrix(np.split(np.array(matrix2arr), 10))
    sns.heatmap(arr)
    plt.show()


state_transition_E5(20000)
