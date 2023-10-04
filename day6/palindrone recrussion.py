def palin(n,l,r):
    if l>r:
       # print("palindrone")
        return True
    if n[l]==n[r]:
        return palin(n,l+1,r-1)
    else:
        #print("not palindrone")
        return False
    
    
n=input("enter a string")
print(palin(n,0,len(n)-1))
