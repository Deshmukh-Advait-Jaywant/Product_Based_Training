num=int(input("enter a number"))
lis=[]
flag=[]
for i in range(0,num):
    n=int(input())
    lis.append(n)
    flag.append(i)
for i in flag:
    if i not in lis:
        print(i)
    
