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
