s=input("enter a string")
print(s[1])
print(s[-1])
print(s[0:])
print(s[:-5])
print(s[-5:])
print(s[:5])
'''output:
enter a stringswathi
w
i
swathi
s
wathi
swath'''

s0="D."
s1="swa"
s2="thi"
print('s0+s1+s2=',s0+s1+s2)
print('s*2=',s*2)
'''output:


count=0
for letter in "swathi is good girl":
    if(letter=='s'):
        count+=1
print("letter count",count)



count=1
for words in "swathi is good girl":
    if(words == ' '):
        count+=1
print("words count",count)
print('i' in 'swa')
print((len(s)))
print(tuple(enumerate(s)))
print(list(enumerate(s)))
print(set(enumerate(s)))
print("i'am 'swathi'")
print('i\'am "swathi"')
print("i'am \"swathi\"")
