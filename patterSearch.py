def Naive_pattern_search(string1,pattern):
    m = len(pattern)
    n = len(string1)
    for i in range(n-m+1):
        j=0
        print(string1[i],pattern[j])
        while(j<m):
            print("matching",string1[i+j],"with",pattern[j])
            if(string1[i+j]!=pattern[j]):
                break
            j+=1

            if (j==m):
                print("pattern found at index",i)




pattern = 'ABAB'
Naive_pattern_search('ABABABCD',pattern)
