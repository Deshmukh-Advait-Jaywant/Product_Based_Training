l=[3,2,1,4,5]
count=0
'''for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count+=1
print(count)
'''
i=0
j=len(l)-1
while(i<=j):
    for j in range(j,i,-1):
        if l[i]>l[j]:
            count=count+1
    i+=1
print(count)
