def check(n,i,target,lis):
    if target==0:
        print(lis)
        return
    if target<0 or i==len(n):
        return
    lis.append(n[i])
    check(n,i+1,target-n[i],lis)
    lis.pop()
    check(n,i+1,target,lis)

n=[10,20,15,5,1,2,3,4,5]
target=50
check(n,0,target,[])
