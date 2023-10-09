def fun(l,low,high):
    if low==high:
        return l[low]
    if low>high:
        return -1
    mid=(low+high)//2
    return fun(l,low,mid)+fun(l,mid+1,high)
    
l=[5,2,7,3,5,7,8]
print(fun(l,0,len(l)-1))


