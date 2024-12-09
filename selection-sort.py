def select(n, s):
    cnt = 0
    for i in range(n - 1):
        minv, minj = s[i], i  #minj is the smallest. minv is to find the min value
        for j in range(i+1, n):
            if s[j] < minv:
                minv, minj = s[j], j
                cnt += 1
        if i != minj:
            s[i], s[minj] = s[minj], s[i]
        
        print(s, cnt)
    return cnt

n = int(input())
s = list(map(int, input().split()))
print(select(n, s))