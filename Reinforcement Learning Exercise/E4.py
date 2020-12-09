import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def reward(state):
    if (state == 100):
        return 100
    else:
        return 0

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


def search(iterations):
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


search(30)