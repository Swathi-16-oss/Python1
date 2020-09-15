s=input("enter a string")
print(s[1])
print(s[-1])
print(s[0:])
print(s[:-5])
print(s[-5:])
print(s[:5])

s="swa"
s1="thi"
print('s+s1=',s+s1)
print('s*2=',s*2)


count=0
for letter in "swathi is good girl":
    if(letter == 's'):
        count+=1
print("letter count",count)



count=1
for words in "swathi is good girl":
    if(words == ' '):
        count+=1
print("words count",count)
print('i' in 'swa')




print(len(s))
print(tuple(enumerate(s)))
print(list(enumerate(s)))
print(set(enumerate(s)))
print("i'am 'swathi'")
print('i\'am "swathi"')
print("i'am \"swathi\"")
