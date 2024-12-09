def select(n, s):
    cnt = 0
    for i in range(n - 1):
        minv, minj = s[i], i  
        for j in range(i+1, n):
            if s[j] < minv:
                minv, minj = s[j], j
        if i != minj:
            s[i], s[minj] = s[minj], s[i]
            cnt += 1
        print(s, cnt)
    return cnt

n = int(input())
s = list(map(int, input().split()))
print(select(n, s))