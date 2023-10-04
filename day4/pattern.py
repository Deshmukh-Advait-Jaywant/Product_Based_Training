'''
i/p=4
o/p:
*
* *
* * *
* * * *
'''
'''
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
'''
#using 1 for loop
'''
n=int(input("enter a number"))
for i in range(n):
    print("* " * (i+1))
'''
'''
a=int(input("enter a number"))
for i in range(a):
    print(" "*(a-i) + "* " *(i+1))
'''

'''
a=int(input("enter a number"))
for i in range(a):
    print(" "*(a-i) + "* " *(i))
for i in range(a):
    print(" "*(i) + "* " *(a-i))
'''


'''

a=int(input("enter a number"))
for i in range(a):
    print(" "*(a-i) + "* " *(i+1))
for i in range(a):
    print(" "*(i+1) + "* " *(a-i))
'''
'''
1
22
333
4444
'''
'''
n=int(input())
for i in range(n):
    print(str(i+1)*(i+1))
'''
'''
n=int(input())
for i in range(1,n+1):
    print(((10**i)//9)*i)
'''
    






