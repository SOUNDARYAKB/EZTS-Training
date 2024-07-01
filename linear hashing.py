input1=list(map(int,input().split()))
n=len(input1)
hash_list=[False]*n
for i in input1:
    h_k=i%n
    for j in range(0,len(hash_list)):
        h1_k=(h_k+j)%n
        if hash_list[h1_k]==False:
            hash_list[h1_k]=i
            break
print(hash_list)