x=int(input())
low=1
high=x
floor=0
while low<=high:
    mid=(low+high)//2
    sq=mid*mid
    if sq==x:
        floor=mid
        break
    elif sq<x:
        floor=mid
        low=mid+1
    else:
        high=mid-1
print(floor)
