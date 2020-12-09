import random

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import time
from matplotlib.patches import Polygon

# 0 - Left
# 1 - Right
# 2 - Up
# 3 - Down

# E1
def state_transition(state, action):
    if (action == 0):
        end_state = state - 1
    elif (action == 1):
        end_state = state + 1
    elif (action == 2):
        end_state = state - 10
    elif (action == 3):
        end_state = state + 10
    else:
        return "Invalid syntax for action"

    if (end_state <= 100 and end_state >= 1):
        agent_reward = reward(end_state)
        return end_state, agent_reward
    else:
        return state, 0


# E2
def reward(state):
    if (state == 100):
        return 100
    else:
        return 0

# E3
def search(iterations):
    accumulated_reward = 0
    average_reward = 0
    state = 1
    for x in range(iterations):
        action = random.randint(0, 3)
        step = state_transition(state, action)
        accumulated_reward = accumulated_reward + step[1]
        state = step[0]

    if (accumulated_reward > 0):
        average_reward = iterations / accumulated_reward

    return accumulated_reward, average_reward


'''
start_time = time.time()
search(100)
print(time.time() - start_time, "seconds")

start_time = time.time()
search(1000)
print(time.time() - start_time, "seconds")

start_time = time.time()
search(10000)
print(time.time() - start_time, "seconds")
'''


# E4
def choose_state(state, vector):
    possible_states = []
    if (state % 10 == 1):
        possible_states.append(state + 1)
    elif (state % 10 == 0):
        possible_states.append(state - 1)
    else:
        possible_states.append(state - 1)
        possible_states.append(state + 1)
    if (state - 10 > 0): possible_states.append(state - 10)
    if (state + 10 <= 100): possible_states.append(state + 10)
    possible_states_utility = []
    for i in possible_states:
        possible_states_utility.append(vector[i - 1])
    m = max(possible_states_utility)
    max_idx = [i for i, j in enumerate(possible_states_utility) if j == m]
    chosen_state = random.choice(max_idx)
    return possible_states[chosen_state]


def search_E4(iterations):
    # V(s) = (1 - alfa) * V(s) + alfa * ( r(s) + discount * V(s') )
    for i in range(iterations):
        average_reward_step_0_lst = []
        average_reward_step_20000_lst = []
        average_reward_step_0 = 0
        average_reward_step_20000 = 0
        vector = [0 for i in range(100)]
        alfa = 0.05
        discount = 0.9
        accumulated_reward = 0
        average_reward = 0
        state = 1
        for x in range(20000):
            if x == 0:
                accumulated_reward_step_0 = 0
                for j in range(1000):
                    next_state = choose_state(state, vector)
                    step_reward = reward(state)
                    accumulated_reward_step_0 = accumulated_reward_step_0 + step_reward
                    if state == 100:
                        state = 1
                    else:
                        state = next_state
                    average_reward_step_0 = accumulated_reward_step_0 / 1000
                    average_reward_step_0_lst.append(average_reward_step_0)
            if x == 19999:
                accumulated_reward_step_20000 = 0
                for k in range(1000):
                    next_state = choose_state(state, vector)
                    step_reward = reward(state)
                    accumulated_reward_step_20000 = accumulated_reward_step_20000 + step_reward
                    if state == 100:
                        state = 1
                    else:
                        state = next_state
                    average_reward_step_20000 = accumulated_reward_step_20000 / 1000
                    average_reward_step_20000_lst.append(average_reward_step_20000)
            next_state = choose_state(state, vector)
            step_reward = reward(state)
            if state == 100:
                vector[state - 1] = (1 - alfa) * vector[state - 1] + alfa * (step_reward + discount * 0)
                state = 1
            else:
                vector[state - 1] = (1 - alfa) * vector[state - 1] + alfa * (
                        step_reward + discount * vector[next_state - 1])
                state = next_state

        arr = np.asmatrix(np.split(np.array(vector), 10))
        sns.heatmap(arr)
        plt.show()

    plt.boxplot([average_reward_step_0_lst, average_reward_step_20000_lst])
    plt.show()


# search_E4(30)

# E5

matrix = [[round(random.uniform(-0.1, 1.0), 2) for j in range(4)] for i in range(100)]
print(matrix)
'''
[LEFT,RIGHT,UP,DOWN]
'''


def choose_state_E5(state):
    possible_states = []
    greed = 0.3
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
            matrix[state - 1][action] = (1 - alfa) * matrix[state - 1][action] + alfa * (action_reward + discount * matrix[next_state - 1][action])
            state = next_state
    matrix2arr=[]
    for i in range(len(matrix)):
        matrix2arr.append(max(matrix[i]))
    arr = np.asmatrix(np.split(np.array(matrix2arr), 10))
    sns.heatmap(arr)
    plt.show()

state_transition_E5(1000)

#E6


