def palin(n):
    l=0
    r=len(n)-1
    while(l<r):
        if n[l]==n[r]:
            l+=1
            r-=1
        else:
            print("not palindrone")
            return
    print("palindrone")
    return



n=input("enter a string")
palin(n)
