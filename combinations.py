def com(li):
    if(len(li)==0):
        return []
    elif(len(li)==1):
        return [li]
    else:
        for i in range(len(li)):
            for j in range(len(li)):
                            for k in range(len(li)):
                                           if(i!=j & j!=k  &k!=i):
                                               print(li[i],li[j])
data=list('134')
print('com')
for j in com(data):
    print(j)
