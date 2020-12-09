import random

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