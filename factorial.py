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
    pass
while(n>0):
    fact=fact*i
    i=i+1
    if(i==n+1):
        break
print(fact)
'''o/p:
enter the number5
 120''' 

import math
n=int(input("enter the number"))
print(math.factorial(n))
def fact(n):
    if(n==1):
        return n
    else:
        facto=n*fact(n-1)
        return facto
 '''o/p:
 enter the number5
 120''' 
n=int(input("enter the number"))
print(fact(n))
print("....%s sec"%(time.time()- start_time))
'''o/p:
enter the number4
24
....3.894068479537964 sec '''   


