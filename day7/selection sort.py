n=list(map(int,input().split()))
l=len(n)
for i in range(l-1):
    mini=i
    for j in range(i+1,l):
        if n[j]<n[mini]:
            mini=j
    n[i],n[mini]=n[mini],n[i]
print(n)
