n=int(input())
k=int(input())
j=int(input())
m=int(input())
p=int(input())
bm=m//k
if m%k!=0:
    bm+=1
pm=p//j
if p%j!=0:
    pm+=1
left=n-(bm+pm)
if left<0:
    left=0
print(f'No of monkeys left is: {left}')
