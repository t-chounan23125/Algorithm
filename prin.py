def prin(n, num= 0):
    if num == n:
        print(n)
    else:
        print(num)
        return(prin(n, num+ 1))
    
    
n = int(input())
prin(n)