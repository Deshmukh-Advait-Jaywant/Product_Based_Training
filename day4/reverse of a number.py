x=int(input("enter a number"))
isnegative=False
if x<0:
    isnegative=True
    x=-x
revNum=0
while x!=0:
    revNum=revNum*10+x%10
    x=x//10
if revNum>=2**30 or revNum<=-2**30:
    print("above 32 bits")

print(-revNum if isnegative else revNum)
