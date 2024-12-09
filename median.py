import random
def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)

# SEED, MIN, MAX, N, K = 2022, 10, 100, 15, 5
# S = generate(SEED, MIN, MAX, N)
# print(S)
def solve(S):
    
    cnt = 0
    while len(S) > N - K - 1:
         

         mid = (len(S) - 1) // 2
         if cnt == K :
            print(S[mid])
         
        # print(S[mid], end = " ")
         S.remove(S[mid])
         cnt += 1
        
        
    
        
  

    
SEED, MIN, MAX, N, K = 2022, 10, 100, 15, 5
S = generate(SEED, MIN, MAX, N)
print(S)
solve(S)

# [78, 46, 66, 79, 49, 84, 17, 76, 98, 62, 97, 91, 50, 11, 65]