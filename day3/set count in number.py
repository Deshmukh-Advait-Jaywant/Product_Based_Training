#decimal to binary
n=int(input("enter a number"))
i=1
rem=0
binary=0
while n!=0:
    rem=n%2
    binary+=rem*i
    i*=10
    n=n//2
binary=str(binary)
count=0
for i in binary:
    if i=='1':
        count+=1
print(count)
