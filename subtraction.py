a=int(input("enter a num"))
b=int(input("enter b number"))
c=a-b
print(c)
'''o/p:
enter a num3
enter b number23
-20'''

a=2
b=8
c=a-b
print(c)
#o/p:-6
a=3
b=5
c=a+b
i=print('sub of {0} and {1} is {2}'.format(a,b,c))
#sub of 3 and 5 is 8
def sub():
    return 5-6
print(sub())
#o/p:-1
def sub(a,b="default"):
    print(a-b)
sub(4,2)
#o/p:2
    

class sub():
    def sub1(self,a,b):
        self.a=a
        self.b=b
        return self.a-self.b
a=int(input("enter a num"))
b=int(input("enter b number"))
obj=sub()
print(obj.sub1(a,b))
'''o/p:
enter a num34
enter b number56
-22'''

class sub():
    def sub1(self,a,b):
        return a-b
a=2
b=7
obj=sub()
print(obj.sub1(a,b))
#o/p:2

