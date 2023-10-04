#functions
'''def cse():
    print("hi")
def ece(x,y):
    print("hello")
ece(5,6,7) #we get a type error
cse()
'''

'''
def cse():
    print("hi")
def ece(*x):
    print("hello",x)#data type of x is tuple
ece(5,6,7) 
cse()
'''

'''
def cse():
    print("hi")
def ece(*x):
    print("hello",x)#data type of x is tuple
ece(5,6,3,5,6,7,) #it will not be error
cse()
'''
#non-default arg should not follow default argdef cse():
#but defalut can be followed by non-default
'''
    print("hi")
def ece(x=1,y):
    print("hello",x)#data type of x is tuple
ece(5,6) #it will not be error
cse()
'''
#controlling recrussion by '' return ''
def cse(x):
    if x==0:
        return 0
    print(x)
    print(cse(x-1))
    print(x)
    return 0
cse(4)





















