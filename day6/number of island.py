l=[[0,1,0,1],[1,1,0,0],[0,0,1,1],[1,0,1,0]]
n=len(l)
"""
for i range(n):
    l.append(list(map(int,input().spilt)))"""
count=0
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    
    if l[i][j]==1:
        l[i][j]=0    
    
    if i>0:
        fun(l,i-1,j,n)
    if i<n-1:
        fun(l,i+1,j,n)     
    if j>0:
        fun(l,i,j-1,n)
    if j<n-1:
        fun(l,i,j+1,n)
        
    
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
            fun(l,i,j,n)
print(count)
