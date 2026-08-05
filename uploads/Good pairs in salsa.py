a='00111101'
b='10000001'
c=0
for i in range(len(a)):
    if a[i] != b[i]:
        c += 1
print(c)
per=c/len(a)*100
print(per)