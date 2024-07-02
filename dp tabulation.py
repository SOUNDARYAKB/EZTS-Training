w=[1,3,5,4,1,3,2]
p=[5,10,15,7,8,9,4]
n=7
c=15
dp=[[0 for i in range(c+1)]for i in range(n+1)]
for i in range(1,n+1):
    for c in range(i,c+1):
        if c-w[i-1]<0:
            dp[i][c]=dp[i-1][c]
        else:
            dp[i][c]=max(dp[i-1][c],p[i-1]+dp[i-1][c-w[i-1]])
print(dp[n][c])                