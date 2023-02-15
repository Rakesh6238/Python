class Rectangle:
    def __init__(self):
        self.l=int(input("enter the length of  rectangle"))
        self.b=int(input("enter the breadth of rectangle:"))
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
    def compare(self,obj2):
        try:
            if obj1.area()==obj2.area():
                print("both areas are equal")
            elif obj1.area()>obj2.area():
                print("area of rectangle is less than rectangule2")
            elif obj1.area()<obj2.area():
                print("area of rectangle is less than rectangular2")
        except:
            print("can't be compared")

obj1=Rectangle()
print("area=",obj1.area())
print("perimeter=",obj1.perimeter())

obj2=Rectangle()
print("area=",obj2.area())
print("perimeter=",obj2.perimeter())

obj1.compare(obj2)
    
    