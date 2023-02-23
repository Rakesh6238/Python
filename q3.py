#2(a)
l=[1,2,3,4,-1,-2]
s=[i for i in l if i>0]
print(s)



#2(b)
a=int(input("enter the number"))
j=[i*i for i in range(a+1)]
print(j)



#2(c)
v=['a','e','i','o','u','A','E','I','O','U']
a=input("enter the text")
s=[i for i in a if i in v]
print(s)

#2(d)
a=input("enter the word")
s=[ord(i) for i in a]
print(s)