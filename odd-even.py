def solve(n, s):
    lower, upper = [], []

    for i in range(n):
        if s[i].isupper() == True:
            upper.append(s[i])
        else:
            lower.append(s[i])

    upper.sort()
    lower.sort(reverse=True)
    print(" ".join(map(str, upper)))
    print(" ".join(map(str, lower)))


N = int(input())
S = input()
solve(N, S)