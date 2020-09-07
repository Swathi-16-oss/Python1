# Python1
a=int(input("enter a number"))
b=int(input("enter b number"))
c=a+b
print(c)


a,b=4,4
c=a+b
print(c)



def add():
    return 4+3
print(add())


def add(a,b='default'):
        print(a+b)
add(2,2)


a="addition of {a} and {b} is {c}".format(a=2,b=6,c=a+b)
print(a)

a=2
b=5
c=a+b
i="addition of {0} and {1} is {2}".format(a,b,c)
print(i)

class add():
    def add1(self,a,b):
        c=a+b
        return c
a=int(input("enter a num"))
b=int(input("enter b num"))
obj=add()
c=obj.add1(a,b)
print(c)


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

a=(1,2)
x=sum(a)
print(x)

