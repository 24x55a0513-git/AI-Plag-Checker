n=int(input())
x,y=0,0
for i in range(1,n+1):
    d=i*10
    if i%4==1:
        x+=d
    elif i%4==2:
        y+=d    
    elif i%4==3:
        x-=d
    else:
        y-=d
print(x,y)