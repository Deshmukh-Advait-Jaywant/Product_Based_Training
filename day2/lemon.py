requried=21
n=int(input("enter number of lemons"))
string="enter correct value"
print(string if n<0 else (n-requried,'more') if n>21 else (requried-n,'less'))
