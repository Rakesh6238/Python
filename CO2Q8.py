list=[]
n=int(input("enter the number of elements in list:"))
for x in range(0,n):
    element=input("enter word "+str(x+1)+":")
    list.append(element)
max1=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print("the word with longest length is:",temp)
print("length of ",temp,"is",len(i))