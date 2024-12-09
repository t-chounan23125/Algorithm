# s = [1, 2, 3 ,4 ,5, 6 ,7 ,8, 9, 1000]
s = list (map(int, input().split()))
s = sorted(s)
print(s[-3])