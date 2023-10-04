c=input("enter a char")
n=int(input("enter the key"))
asci=ord(c)+n
if asci>122:
    print(chr(ord(c)+n-26))
else:
    print(chr(ord(c)+n))


