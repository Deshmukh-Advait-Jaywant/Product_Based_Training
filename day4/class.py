'''class cse:
    pass

a=cse()
print(a)#it gives the reference of the object
'''
'''
class cse:
    def qwer(self):
        print("hi")
a=cse()
#calling method using objects
a.qwer()
cse.qwer(a)
'''
#variable linked with object is non-static
#constructor
class cse:
    x=30
    def __init__(self,k):
        self.y=k
    def qwer(self):
        print("hi")
a=cse(80)
a.qwer()
print(cse.x,a.y)
#y should be accessed with a variable or lese we will get an error
#if we dont use object of accessing x we dont get error as it is a static variable


#a.qwer here the a object is holded by self 





















