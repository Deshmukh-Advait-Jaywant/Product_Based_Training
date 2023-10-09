def binary(low,high,l,search):
    mid=(low+high)//2
    if low>=high:
        return l[mid+1]
    if l[mid]==search:
        return l[mid+1]
    if l[0]>search:
        return -1
    elif l[mid]>search:
        return binary(low,mid-1,l,search)
    elif l[mid]<search:
        return binary(mid+1,high,l,search)
            
    
l=[5,8,9]
search=6
print(binary(0,len(l)-1,l,search))
