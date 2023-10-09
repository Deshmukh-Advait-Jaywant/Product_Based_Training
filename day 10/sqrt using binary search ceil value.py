x=int(input())
low=1
high=x
ceil=0
while low<=high:
    mid=(low+high)//2
    sq=mid*mid
    if sq==x:
        ceil=mid
        break
    elif sq<x:
        ceil=mid+1
        low=mid+1
    else:
        high=mid-1
print(ceil)
