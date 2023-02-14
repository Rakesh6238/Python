#using recursion
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
num=int(input("Enter a No:"))
print("The Factorial of",num,"is",calc_factorial(num))



#n=int(input("enter the number:"))
#fact=1
#for i in range(1,n+1):
    #fact=fact*i
#print("factorial=",fact)    
    
