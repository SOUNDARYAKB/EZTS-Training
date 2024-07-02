k=[22,10,47,42,56,100,50,92,99]
res=[False]*len(k)
for i in k:
    hk=i%10
    print(hk)
    if res[hk]==False:
        res[hk]=i
    else:
        res[hk+1]=i
        print(res)    
