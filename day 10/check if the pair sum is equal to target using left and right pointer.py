l=[2,3,5,6,8,10]
left=0
right=len(l)-1
target=15
while left<right:
    if l[left]+l[right]==target:
        print(left,right)
        break
    elif l[left]+l[right]<target:
        left+=1
    else:
        right-=1
