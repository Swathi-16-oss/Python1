import time
start_time=time.time()
n=int(input("enter the number"))
fact=1
if(n==0):
    print(fact)
else:
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
'''o/p:
enter the number5
 120'''       

n=int(input("enter the number"))
i=1
fact=1
if(n==0):
    print(fact)
while(n>0):
    fact=fact*i
    i=i+1
    if(i==n+2):
        break
    print(fact)
    
import math
n=int(input("enter the number"))
print(math.factorial(n))
def fact(n):
    if(n==1):
        return n
    else:
        facto=n*fact(n-1)
        return facto
n=int(input("enter the number"))
print(fact(n))


print("....%s sec"%(time.time()- start_time))
    


