def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum 

n = int(input())
print(sum(n))