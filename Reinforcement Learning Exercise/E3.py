import random
import E1
import E2
import seed

# 0 - Left
# 1 - Right
# 2 - Up
# 3 - Down

random.seed(seed.seed)
def search(iterations):
    accumulated_reward = 0
    avg_reward = 0
    state = 1
    for x in range(iterations):
        if state == 100:
            state = 1

        action = random.randint(0, 3)
        state = E1.state_transition(state, action)
        rwd = E2.reward(state)
        accumulated_reward = accumulated_reward + rwd
    if accumulated_reward > 0:
        avg_reward = iterations / accumulated_reward

    return accumulated_reward, avg_reward

import time
import numpy as np
import matplotlib.pyplot as plt

itr = [1000, 20000]
for k in itr:
    runtimes = []
    for j in range(30):
        start_time = time.time()
        run = search(k)
        end_time = time.time() - start_time
        runtimes.append(end_time)
        print('Run:',j+1,'For', k, 'iterations - Accumulated reward: ', run[0], 'Average reward: ', round(run[1],2), 'Time:', end_time)
    print('Average run-times:',sum(runtimes)/30,'Standard deviation:', np.std(runtimes), 'Iterations:',k)
    plt.boxplot(runtimes)
    plt.show()

