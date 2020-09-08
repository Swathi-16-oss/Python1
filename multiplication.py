a=int(input("enter a num"))
b=int(input("enter b number"))
c=a*b
print(c)

a=2
b=8
c=a*b
print(c)

a=3
b=5
c=a*b
i=print('sub of {0} and {1} is {2}'.format(a,b,c))

def mul():
    return 5*6
print(mul())



def mul(a,b="default"):
    print(a*b)
mul(4,2)

    

class mul():
    def mul1(self,a,b):
        self.a=a
        self.b=b
        return self.a*self.b
a=int(input("enter a num"))
b=int(input("enter b number"))
obj=mul()
print(obj.mul1(a,b))


class mul():
    def mul1(self,a,b):
        return a*b
a=9
b=7
obj=mul()
print(obj.mul1(a,b))



