class Rectangle:
    def __init__(self):
        self.__l=int(input("enter the length of  rectangle"))
        self.__b=int(input("enter the breadth of rectangle:"))
    def __lt__(self,obj2):
        area1=self.__l*self.__b
        area2=obj2.__l*obj2.__b
        print("Area of Rectangle1 is ",area1)
        print("Area of Rectangle2 is ",area2)
        return area1<area2
print("Enter the length and breadth of first object :")
obj1=Rectangle()
print("Enter the length and breadth of second object :")
obj2=Rectangle()
if obj1<obj2:
    print("obj1 is less than obj2")
else:
    print("obj1 is greater than obj2")
        