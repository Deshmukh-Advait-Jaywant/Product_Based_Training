def check(n,i,target):
    if target==0:
        return 1
    if target<0:
        return 0
    if i==len(n):
        return 0
    return check(n,i+1,target-n[i]) + check(n,i+1,target)
n=[10,20,15,5]
target=80
print(check(n,0,target))
