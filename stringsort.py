import random
from string import ascii_lowercase

def generate(SEED, N):
    random.seed(SEED)
    S=[]
    for _ in range(N):
        length=random.randint(1, N-1)
        s=random.sample(ascii_lowercase, length)
        S.append("".join(s))
    return S

S=generate(2002,10)
print(S)
# ['q', 'yusdij', 'd', 'qjcbk', 'lapyft', 'yltqwsx', 'wborail', 'otaskimlz', 'd', 'wmnpz']