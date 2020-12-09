import random
import time
from E1 import bit_pattern
from E3 import evaluate_pattern

def bit_pattern(size):
    string = ""
    for i in range(size):
        string = string + str(random.randint(0, 1))
    return string

def mutate(pattern_to_mutate):
    mutation = list(pattern_to_mutate)
    bit_to_flip = random.randint(0, len(mutation) - 1)
    if mutation[bit_to_flip] == "1":
        mutation[bit_to_flip] = "0"
    else:
        mutation[bit_to_flip] = "1"
    mutated = "".join(mutation)

    return mutated


def generate_population(pattern_size, population_size):
    pattern_lst = []
    for i in range(population_size):
        pattern_lst.append(bit_pattern(pattern_size))
    return pattern_lst


def get_best_population(pattern_lst, guess, pattern_size, population_size):
    proximity_lst = []

    for i in range(len(pattern_lst)):
        proximity_lst.append(evaluate_pattern(guess, pattern_lst[i]))

    best_population = []
    current_proximity = 100
    possible_proximity = 100 / pattern_size
    #possible_proximity_round = round(possible_proximity, 0)
    while len(best_population) < population_size * 0.3:
        for i in range(len(proximity_lst)):
            if proximity_lst[i] == current_proximity:
                best_population.append(pattern_lst[i])
        if current_proximity == 0:
            break
        else:
            current_proximity = current_proximity - possible_proximity

    best_individual = pattern_lst[proximity_lst.index(max(proximity_lst))]
    return best_population, int(max(proximity_lst)), best_individual


def E6(pattern_size, guess, population_size):
    pattern_lst = generate_population(pattern_size, population_size)
    best_population = get_best_population(pattern_lst, guess, pattern_size, population_size)
    best_population_lst = best_population[0]
    max_proximity = best_population[1]
    best_individual = best_population[2]
    stagnate = 0
    iterations = 0
    while stagnate != 200000:
        print(stagnate)
        new_population = []
        while len(new_population) < 100:
            pattern_to_mutate_idx = random.randint(0, len(best_population_lst) - 1)
            new_population.append(mutate(best_population_lst[pattern_to_mutate_idx]))
        best_population = get_best_population(new_population, guess, pattern_size, len(new_population))
        best_population_lst = best_population[0]
        if guess == best_population[2]:
            print('found')
            break
        elif max_proximity <= best_population[1]:
            stagnate = stagnate + 1
        else:
            max_proximity = best_population[1]
            best_individual = best_population[2]
            stagnate = 0
        iterations = iterations + 1
    print(best_population[2], guess, iterations)

E6(32, bit_pattern(32), 100)
