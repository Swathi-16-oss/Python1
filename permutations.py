from itertools import permutations
str= permutations(['s', 'o','w'])
for p in list(str):
    print(p)

    

def per(li):
    if(len(li)==0):
        return []
    elif(len(li)==1):
        return [li]
    else:
        lis=[]
        for i in range(len(li)):

            x=li[i]
            x1=li[:i]+li[i+1:]
            for j in per(x1):
                lis.append([x]+j)
         return lis
data=list('123')
print('per')
for j in per(data):
    print(j)
