from E1 import bit_pattern
from E3 import evaluate_pattern
from E6 import generate_population, get_best_population, mutate
import random

def crossover(pattern_size, guess, population_size):
    pattern_lst = generate_population(pattern_size, population_size)
    best_population = get_best_population(pattern_lst, guess, pattern_size, population_size)
    best_population_lst = best_population[0]
    max_proximity = best_population[1]
    stagnate = 0
    mutation_rate = 0.05
    iterations = 0
    while stagnate < 20000:

        new_population = best_population_lst
        while len(new_population) != population_size:
            parent_1 = random.choice(best_population_lst)
            parent_2 = random.choice(best_population_lst)
            idx = random.randint(0, len(parent_1)-1)
            parent_1 = parent_1[idx:]
            parent_2 = parent_2[:idx]
            cross = parent_1 + parent_2
            new_population.append(cross)
        for i in range(len(best_population_lst)):
            mutation = random.random()
            if mutation < mutation_rate:
                new_population[i] = mutate(new_population[i])
        best_population = get_best_population(new_population, guess, pattern_size, len(new_population))
        best_population_lst = best_population[0]
        max_proximity = best_population[1]
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
        print(best_population[2], '-', guess, '-', max_proximity, '-', iterations)

crossover(32, bit_pattern(32), 100)