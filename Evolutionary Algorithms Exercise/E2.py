import random

def guess_pattern(pattern):
    guess = ""
    tries = 0
    while guess != pattern:
        guess = ""
        tries = tries + 1
        for i in range(len(pattern)):
            guess = guess + str(random.randint(0, 1))
    return tries
