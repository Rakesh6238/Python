import functionn
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Choose \n 1.Addition \n 2.Substraction\n 3.Multiplication \n 4.Division"))
if c==1:
    s1=(functionn.sum(a,b))
    print("sum=",s1)
elif c==2:
    s2=(functionn.sub(a,b))
    print("sub=",s2)
elif c==3:
    s3=(functionn.mul(a,b))
    print("mul=",s3)    
elif c==4:
    s4=(functionn.div(a,b))
    print("div=",s4)    
