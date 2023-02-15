fn=open("abc1.txt",'w')
fn.write("1.python is an amazing language \n2.it is very easy to learn. \n3.1234567890")
fn.close()
fn1=open("abc1.txt",'r')
f=fn1.readlines()
#print(f)
for x in range(0,len(f)):
    print(f[x])
fn1.close()
