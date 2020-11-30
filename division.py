a=int(input("enter a num"))
b=int(input("enter b number"))
c=a/b
print(c)
'''o/p:
enter a num45
enter b number3
15.0'''

a=2
b=8
c=a/b
print(c)
#o/p:0.25

a=3
b=5
c=a/b
i=print('division of {0} and {1} is {2}'.format(a,b,c))
#o/p:division of 3 and 5 is 0.6


def div():
    return 5/6
print(div())
#o/p:0.8333333333333334



def div(a,b="default"):
    print(a/b)
div(4,2)
#o/p:2.0


    

class div():
    def div1(self,a,b):
        self.a=a
        self.b=b
        return self.a/self.b
a=int(input("enter a num"))
b=int(input("enter b number"))
obj=div()
print(obj.div1(a,b))
'''o/p:
enter a num6
enter b number3
2.0
'''

class div():
    def div1(self,a,b):
        return a/b
a=9
b=7
obj=div()
print(obj.div1(a,b))
#o/p:1.2857142857142858
