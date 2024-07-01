input1=[20,34,45,70,56,81,67,37,46,39,54]
print(input1)
hash_list=[False]*11
for i in input1:
    h1_k=i%11
    if hash_list[h1_k]==False:
        hash_list[h1_k]=i
    else:
        h2_k=8-(i%8)
        for j in range(1,10):
            h_k=(h1_k+j*h2_k)%11
            if hash_list[h_k]==False:
                hash_list[h_k]=i
                break
print(hash_list)