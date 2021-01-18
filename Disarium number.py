num=int(input("enter"))
n=num#make a copy of number
count=len(str(num))#to count no of digits in integer 
rem=sum=0
while(num>0):
    rem=num%10  #remainder  
    sum=sum+(rem**count)   
    num=num//10    
    count=count-1
#if sum is equal to number then it is diasarium  
if(sum == n):
    print(str(n) + " is a disarium number")    
else:
    print(str(n) + " is not a disarium number")


'''explanation:
135
1^1+3^2+5^3
1+9+125
sum=135
so sum is equal to n so it is disarium.
o/p:
enter135
135 is a disarium number
>>>
enter89
89 is a disarium number


>>> 
enter123
123 is not a disarium number'''

