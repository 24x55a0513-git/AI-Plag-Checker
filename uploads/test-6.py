n=int(input())
nums=list(map(int,input().split()))
c=None
k=0
for i in nums:
    if k==0:
        c=i
    if i==c:
        k+=1
    else:
        k-=1
print(c)
