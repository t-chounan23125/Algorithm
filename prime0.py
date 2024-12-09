def prime(N, M):
    S = [_ for _ in range(N, M +1)]
    
    R = []
    
    for j in range (M - N ) :
        cnt = 0
        for i in range (2, int(S[j] ** 0.5)+ 1):
            
            if S[j] % i == 0 :
                cnt +=1
    
          
        
        if cnt == 0 :
            R.append(S[j])
            

    R.sort(reverse=True)


    for i in range (len(R)) :
        print (R[i], end=" ")
    print()

N, M = map(int, input().split())
prime(N, M)


    