coins=[1,5,7]
amount=18
res={1:0,5:0,7:0}
while amount>0:
    m=coins.pop(coins.index(max(coins)))
    c=amount//m
    res[m]+=c
    amount=amount%m
print(res)    