def solve(n):
    anagrams = {}
    nonanagrams = []
    anadics = {}
    lst = []
    for _ in range(n):
        word1 = input()
        word1 = word1.lower()
        word2 = "".join(sorted(word1))
        if word2 in anadics.keys():
            anadics[word2] += 1
                
        else:             
            nonanagrams.append(word1)
            anagrams[word1] = word2
            anadics.setdefault(word2, 1)
    print(anagrams)
    print(anadics)
    
    for v in anagrams.keys():
         lst.append(v)
    x = sorted(lst)
    print(x)
    
    for str in x:
         if str in anagrams.keys():
            k = anagrams[str]

         if k in anadics.keys():
             print(str, anadics[k])
       
N = int(input())
solve(N)

#run time error
