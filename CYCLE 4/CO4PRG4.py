class Time:
    def __init__(self):
        self.__h=int(input("enter time in hours:"))
        self.__m=int(input("enter time in minutes:"))
        self.__s=int(input("enter time in Seconds:"))
    def __add__(self,obj2):
        hours=self.__h + obj2.__h
        print("Total hours=",hours)
        minutes=self.__m + obj2.__m
        print("Total minutes=",minutes)
        seconds=self.__s + obj2.__s
        print("Total Seconds=",seconds)
        if hours>=24:
            hours=hours%24
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours,minutes,seconds
print("enter the time of  1st object:")
obj1=Time()
print("enter the time 2nd objects:")
obj2=Time()
print("Sum of two Time is:",obj1+obj2)
 
            
        
    