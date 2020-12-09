import random


def evaluate_pattern(guess, pattern):
    pattern_size = len(pattern)
    percentage = 100 / pattern_size
    proximity = 0

    for i in range(pattern_size):
        if guess[i] == pattern[i]:
            proximity = proximity + percentage

    return proximity


def mutate(guess, pattern):
    proximity = evaluate_pattern(guess, pattern)
    mutations = 0
    while proximity < 100:
        mutation = list(guess)
        bit_to_flip = random.randint(0, len(mutation) - 1)
        if mutation[bit_to_flip] == "1":
            mutation[bit_to_flip] = "0"
        else:
            mutation[bit_to_flip] = "1"
        mutation_proximity = evaluate_pattern(mutation, pattern)

        if mutation_proximity > proximity:
            print(str(proximity) + "-" + str(mutation_proximity))
            proximity = mutation_proximity
            guess = "".join(mutation)

        mutations = mutations + 1
    return guess, proximity, mutations


print(mutate("000000000000000", "111111111111111"))
