def check(n,i,target,lis):
    if target==0:
        print(lis)
        return
    if target<0 or i==len(n):
        return
    lis.append(n[i])
    return check(n,i+1,target-n[i],lis)
    return check(n,i+1,target,lis)
n=[10,20,15,5]
target=25
lis=[]
check(n,0,target,lis)
