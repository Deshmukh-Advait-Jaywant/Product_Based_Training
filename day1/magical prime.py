class baby1:
    def magicPrime(self):
        def prime(n):
            for i in range(2,n):
                if n%i==0:
                    return True
                else:
                    return False
        num=input("enter a number")
        rev=num[::-1]
    
        num1=int(num)
        rev1=int(rev)
        
        flag1=prime(num1)
        flag2=prime(rev1)
        if flag1== False and flag2==False:
            print("magic numbers")
        else:
            print("not magic numbers")

class baby2:
    def jwels(self):
       number=int(input("enter a number"))
       for i in range(0,number+1):
            sq=i*i
            sum=0
            while sq>0:
                sum=sum+sq%10
                sq=sq//10
            if i==sum:
                print(i)
   

b1=baby1()
b1.magicPrime()
b2=baby2()
b2.jwels()
