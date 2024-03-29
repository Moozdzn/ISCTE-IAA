import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

random.seed(100)


'''
[LEFT,RIGHT,UP,DOWN]
'''


def reward(state):
    if state == 100:
        return 100
    else:
        return 0


def generate_heatmap(matrix):
    matrix2arr = []
    for j in range(len(matrix)):
        matrix2arr.append(max(matrix[j]))
    arr = np.asmatrix(np.split(np.array(matrix2arr), 10))
    sns.heatmap(arr)
    plt.show()
    return arr


def choose_state(state, matrix, greed):
    possible_states = []
    if state % 10 == 1:
        possible_states.append(1)
    elif state % 10 == 0:
        possible_states.append(0)
    else:
        possible_states.append(0)
        possible_states.append(1)
    if state - 10 > 0: possible_states.append(2)
    if state + 10 <= 100: possible_states.append(3)
    possible_states_utility = []
    for i in possible_states:
        possible_states_utility.append(matrix[state - 1][i])
    is_greedy = random.random()
    if greed > is_greedy:
        m = max(possible_states_utility)
        max_idx = [i for i, j in enumerate(possible_states_utility) if j == m]
        chosen_state = random.choice(max_idx)
        return possible_states[chosen_state]
    else:
        return random.choice(possible_states)


def state_transition(iterations, env, greed):
    state = 1
    alfa = 0.1
    discount = 0.99
    next_state = 0
    increase_greed = False
    if greed == .3: increase_greed = True

    for i in range(iterations):

        if i > iterations * .3 and increase_greed and greed < 1:
            greed = greed + 1/(20000*.7)
            print(greed)

        if state == 100:
            action_reward = reward(state)
            env[state - 1][action] = (1 - alfa) * env[state - 1][action] + alfa * (action_reward + discount * 0)
            state = 1

        else:
            action = choose_state(state, env, greed)
            if action == 0:
                next_state = state - 1
            elif action == 1:
                next_state = state + 1
            elif action == 2:
                next_state = state - 10
            elif action == 3:
                next_state = state + 10
            print(state, next_state)
            action_reward = reward(state)
            env[state - 1][action] = (1 - alfa) * env[state - 1][action] + alfa * (
                    action_reward + discount * max(env[next_state - 1]))
            state = next_state



for t in range(30):
    greed = .9
    util_matrix = [[round(random.uniform(-.1, .1), 2) for h in range(4)] for k in range(100)]
    state_transition(20000, util_matrix, greed)
    generate_heatmap(util_matrix)


'''for t in range(30):
    greed = .2
    util_matrix = [[round(random.uniform(-.1, .1), 2) for h in range(4)] for k in range(100)]
    state_transition(20000, util_matrix, greed)
    #generate_heatmap(util_matrix)
'''

'''for t in range(30):
    greed = .3
    util_matrix = [[round(random.uniform(-.1, .1), 2) for h in range(4)] for k in range(100)]
    state_transition(20000, util_matrix, greed)
    generate_heatmap(util_matrix)'''
