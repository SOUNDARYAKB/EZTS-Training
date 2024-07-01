#give an integer array ,your task is to find the n consecutive/continuous digits which gives u the maximum sum
l=[2,3,4,5,6,7,8,9,8]
sum=max=0
k=int(input("Enter the no of continious digit: "))
for i in range(0,len(l)-(k-1)):
    sum=0
    for j in range(0,k):
        sum+=l[i+j]
    if max<sum:
        max=sum
        pos=i
print("the sum of continous digits which gives max value is:",max)
for j in range(0,k):
    print(l[pos+j])