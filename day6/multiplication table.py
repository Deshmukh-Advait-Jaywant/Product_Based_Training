def table(n,i):
    if i==1:
        return
    
    table(n,i-1)
    print(n*i)
table(2,10)
