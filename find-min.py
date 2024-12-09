import random
SEED, MIN, MAX, N = input().split(" ")
SEED, MIN, MAX, N = int(SEED), int(MIN), int(MAX), int(N)

random.seed(SEED)
S = random.sample(range(MIN, MAX), N)

print(min(S), S.index(min(S)))
