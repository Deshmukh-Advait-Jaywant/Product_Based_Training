a=[1,5,7]
b=[2,4,6]
res=[]
i,j,k=0,0,0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1
res.extend(a[i:])
res.extend(b[j:])

a=res
print(a)
