arr=[2,3,1,2,4,3]
t=7 #target
l=0 #left pointer
ws=0 # min window size
ml=float('inf')
for r in range(len(arr)):
    ws+=arr[r]
    while ws>=t:
        if r-l+1<ml:
            ml=r-l+1
        ws-=arr[l]
        l+=1
print(ml)