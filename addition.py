# Python1
a=int(input("enter a number"))
b=int(input("enter b number"))
c=a+b
print(c)

'''o/p:
enter a number5
enter b number6
11'''



a,b=4,4
c=a+b
print(c)
#0/p:8

def add():
    return 4+3
print(add())
#o/p:7


def add(a,b='default'):
        print(a+b)
add(2,2)
#o/p:4


a=2
b=5
c=a+b
i="addition of {0} and {1} is {2}".format(a,b,c)
print(i)

'''o/p:
addition of 2 and 5 is 7'''

 

class add():
    def add1(self,a,b):
        c=a+b
        return c
a=int(input("enter a num"))
b=int(input("enter b num"))
obj=add()
c=obj.add1(a,b)
print(c)
''o/p:
enter a num4
enter b num5
9'''



class add():
    def add1(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
a=int(input("enter a num"))
b=int(input("enter b num"))
obj=add()
c=obj.add1(a,b)
print(c)
'''o/p:
enter a num6
enter b num7
13'''


a=(1,5)
x=sum(a)
print(x)
#o/p:3
