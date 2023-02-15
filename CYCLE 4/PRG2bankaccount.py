class bank:
    def __init__(self,ac,name,atype,bal=0):
        self.ac=ac
        self.name=name
        self.atype=atype
        self.bal=bal
    def deposit(self,bal):
         self.bal+=bal
    def  withdraw(self,bal):
        if(self.bal==0):
            print("Insufficient Balance!!!")
        elif(self.bal<bal):
            print("Insufficient Balance!!!")
        else:
            self.bal-=bal
    def display(self):
        print("Account Number:",self.ac)
        print("Name:",self.name)
        print("Account Type:",self.atype)
        print("Account Balance:",self.bal)

ac=int(input("Enter Your Account Number:"))
name=input("Enter Your Name:")
atype=input("Enter  Your Account Type(savings/current):")
b1=bank(ac,name,atype)
while(True):
    print("Enter your Choice")
    print("1:Deposit")
    print("2:Withdraw")
    print("3:View")
    print("4:Exit")
    c=int(input())
    if(c==1):
        amount=int(input("Enter the amount to Deposit:"))
        b1.deposit(amount)
        print("Deposited amount =",amount)
    elif(c==2):
        amount1=int(input("Enter the amount to Withdraw:"))
        b1.withdraw(amount1)
    elif(c==3):
       b1.display()
    else:
        exit(0)
   
