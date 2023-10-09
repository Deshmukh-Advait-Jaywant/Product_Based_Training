x=int(input())
low=1
high=x
epsilon=1e-5
while abs(low-high)>epsilon:
    mid=(low+high)/2
    sq=mid*mid
    if sq<x:
        low=mid
    else:
        high=mid
print((low+high)/2)
