G=[    #  1  2   3   4   5   6   7  8   9  10
            [ 0, 7,False,False,False,False,False, 2,False,False],#1
            [ 7, 0,  4,  1,False,  5,False,-1,False,False],#2
            [-1, 4,  0,False,False,False,False, 8,False,False],#3
            [-1, 1,False,  0,  6,  8,  3, 3,False,False],#4
            [-1,-1,False,  6,  0,False,False, 6,  8,False],#5
            [-1, 5,False,  8,False,  0,False,-1,False,False],#6
            [-1,-1,False,  3,False,False,  0,-1,  9,  2],#7
            [2,False,  8,  3,  6,False,False, 0,False,False],#8
            [-1,-1,False,False,  8,False,  9,-1,  0,False],#9
            [-1,-1,False,False,- 1,False,  2,False,False, 0]#10

]

temp={}
for i in range(len(G)):
    temp[i]=float("inf")
Dist=[float("inf")]*len(G)
temp[0]=0  #consider the start index 0

while len(temp)>0:
    min_value=min(temp.values())
    min_key=min(temp,key=temp.get)
    temp.pop(min_key)
    Dist[min_key]=min_value
    for j in range(len(G[min_key])):
        if G[min_key][j]!=False and G[min_key][j]!=0:
            new_dist=min_value+G[min_key][j]
            if j in temp.keys() and temp[j]>new_dist:
                temp[j]=new_dist

print(Dist)    