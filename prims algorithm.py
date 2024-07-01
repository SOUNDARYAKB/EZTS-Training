Graph=[    #  1  2   3   4   5   6   7  8   9  10
            [ 0, 7, -1, -1, -1, -1, -1, 2, -1, -1],#1
            [ 7, 0,  4,  1, -1,  5, -1,-1, -1, -1],#2
            [-1, 4,  0, -1, -1, -1, -1, 8, -1, -1],#3
            [-1, 1, -1,  0,  6,  8,  3, 3, -1, -1],#4
            [-1,-1, -1,  6,  0, -1, -1, 6,  8, -1],#5
            [-1, 5, -1,  8, -1,  0, -1,-1, -1, -1],#6
            [-1,-1, -1,  3, -1, -1,  0,-1,  9,  2],#7
            [2, -1,  8,  3,  6, -1, -1, 0, -1, -1],#8
            [-1,-1, -1, -1,  8, -1,  9,-1,  0, -1],#9
            [-1,-1, -1, -1,- 1, -1,  2, -1, -1, 0]#10
]

visited=[False]*len(Graph)
min=float('inf')
print(min)
for i in range(len(Graph)):
    for j in range(len(Graph[i])):
        if Graph[i][j]==0 or Graph[i][j]==-1:
            continue
        if min>Graph[i][j]:
            min=Graph[i][j]
            x=i
            y=j
print(x+1,y+1,min)

visited[x]=True
visited[y]=True
MST=[]
MST.append(tuple((x+1,y+1,min)))
while False in visited:
    min=float('inf')
    for i in range(len(visited)):
        if visited[i]==True:
            for j in range(len(Graph[i])):
                if Graph[i][j]==0 or Graph[i][j]==-1 or visited[j]==True:
                    continue
                elif min>Graph[i][j]:
                    min=Graph[i][j]
                    x=i
                    y=j
    visited[y]=True
    MST.append(tuple((x+1,y+1,min)))
for i in MST:
    print(i)