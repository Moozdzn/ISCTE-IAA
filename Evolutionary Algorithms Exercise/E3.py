def evaluate_pattern(guess, pattern):
    pattern_size = len(pattern)
    percentage = 100 / pattern_size
    proximity = 0

    for i in range(pattern_size):
        if guess[i] == pattern[i]:
            proximity = proximity + percentage

    return proximity
