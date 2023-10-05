def check(n,i,target):
    if target==0:
        return True
    if target<0:
        return False
    if i==len(n):
        return False
    return check(n,i+1,target-n[i]) or check(n,i+1,target)
n=[10,20,15,5]
target=80
print(check(n,0,target))
