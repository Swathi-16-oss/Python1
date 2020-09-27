a=int(input("enter a num"))
b=int(input("enter b number"))
c=a/b
print(c)

a=2
b=8
c=a/b
print(c)

a=3
b=5
c=a/b
i=print('division of {0} and {1} is {2}'.format(a,b,c))

def div():
    return 5/6
print(div())

def div(a,b="default"):
    print(a/b)
div(4,2)

    

class div():
    def div1(self,a,b):
        self.a=a
        self.b=b
        return self.a/self.b
a=int(input("enter a num"))
b=int(input("enter b number"))
obj=div()
print(obj.div1(a,b))


class div():
    def div1(self,a,b):
        return a/b
a=9
b=7
obj=div()
print(obj.div1(a,b))
