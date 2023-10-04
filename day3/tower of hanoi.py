def hanoi(n,src,aux,des):
    count=1
    if n==1:
        print("move the disk from src: ",src,"to aux :",aux,"to des: ",des)
        return 1
    
    count+=hanoi(n-1,src,des,aux)
    print("move the disk from src: ",src,"to aux :",aux,"to des: ",des)
    count+=hanoi(n-1,aux,src,des)
    return count
n=int(input("enter the value of n"))
print(hanoi(n,'A','B','C'))
