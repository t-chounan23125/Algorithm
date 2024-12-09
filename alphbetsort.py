# N,S = input().split("  ")
# N,S = int(N), S


# def solve(N, S):
#     lower, upper = [], []

#     for i in range(N):
#         if S[i].isupper() == True:
#             upper.append(S[i])
#         else:
#             lower.append(S[i])

#     upper.sort()
#     lower.sort(reverse=True)
#     print("".join(map(str, upper)),end=" ")
#     print("".join(map(str, lower)))

# N,S = input().split("  ")
# N,S = int(N), S
# solve(N,S)
# def solve(N, S):
#     lower, upper = [], []
#     for i in range(N):
#         if S[i].isupper() == True:
#             upper.append(S[i])
#         else:
#             lower.append(S[i])

#     upper.sort()
#     lower.sort(reverse=True)
#     print("".join(map(str, upper)),end=" ")
#     print("".join(map(str, lower)))
# N, S = input().split("  ")
# N, S = int(N), S
# solve(N,S)
def solve(N, S):
    lower, upper = [], []
    for i in range(N):
        if S[i].isupper() == True:
            upper.append(S[i])
        else:
            lower.append(S[i])

    upper.sort()
    lower.sort(reverse=True)
    print("".join(map(str, upper)))
    print("".join(map(str, lower)))
N, S = int(input()), input()

solve(N,S)