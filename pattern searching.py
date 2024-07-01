def KMPAlgo(P,S):
    M=len(P)
    N=len(S)
    lps=[]
    LPS(P,M,lps)
    print(lps)
    i=0
    j=0

    while (N-i)>=(M-j):
        if P[j]==S[i]:
            i+=1
            j+=1
        if j==M:
            print("patter found",i-j)
            j=lps[j-1]
        elif i<N and P[j]!=S[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
def LPS(P,M,lps):
    lps.append(0)
    j=0

    for i in range(1,M):
        if S[i]==P[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j)        


if __name__=="__main__":
    S="CDEABABCABCABCABDAA"
    P="ABCAB"
    KMPAlgo(P,S)