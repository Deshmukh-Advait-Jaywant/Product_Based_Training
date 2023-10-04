'''
give a binary matrix with 1's and 0's
1's ---> trees
0's-----> land
l[r][c] is the starting index of fire

fire moves in top, down,left, right only

1 0 0 1
1 0 0 0
1 0 1 0
0 1 1 1

r=0
c=0

the output is 5

1 0 0 1
1 0 0 1
1 1 1 0
0 1 1 1

r=0
c=0

the output is 2
'''

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
        
l=[[0,0,0,1],[1,0,0,0],[1,1,1,0],[0,1,1,1]]
n=len(l)
r=0
c=0
count=0
if l[r][c]==1:
    fun(l,r,c,n)
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
print(count)
