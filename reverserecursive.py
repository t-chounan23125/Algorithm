def prin(n, num = 0):
    if n == num:
        return None
    else:
        print(n - num, end=" ")
        return prin(n, num + 1)
    
n = int(input())
prin(n)