import random
import E6

'''
[LEFT,RIGHT,UP,DOWN]
'''

def get_possible_states(state, matrix, maze):
    possible_states = []
    if state % 10 == 2 or state % 10 == 6:
        possible_states.append(0)
    if state % 10 == 4 or state % 10 == 8:
        possible_states.append(1)
    if state % 10 == 1:
        possible_states.append(1)
    elif state % 10 == 0:
        possible_states.append(0)
    else:
        possible_states.append(0)
        possible_states.append(1)
    if state - 10 > 0: possible_states.append(2)
    if state + 10 <= 100: possible_states.append(3)
    return possible_states


def choose_state(state, matrix, greed):
    possible_states = get_possible_states(state, matrix)
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
            greed = greed + 1 / (20000 * .7)
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


'''
[LEFT,RIGHT,UP,DOWN]
'''
# Fig 1
util_matrix = [[round(random.uniform(-.1, .1), 2) for h in range(4)] for k in range(100)]

E6.state_transition(20000, util_matrix_1, .8)
E6.generate_heatmap(util_matrix_1)
'''for i in range(len(util_matrix_1)):
    print(util_matrix_1[i],i)'''
