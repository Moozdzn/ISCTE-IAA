# 0 - Left
# 1 - Right
# 2 - Up
# 3 - Down


def state_transition(state, action):
    if action == 0:
        end_state = state - 1
    elif action == 1:
        end_state = state + 1
    elif action == 2:
        end_state = state - 10
    elif action == 3:
        end_state = state + 10
    else:
        return "Invalid syntax for action"

    if 100 >= end_state >= 1:
        return end_state
    else:
        return state
