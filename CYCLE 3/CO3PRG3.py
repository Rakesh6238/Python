from graphics.rectangle import*
from graphics.circle import*
from graphics.threeDgraphics.cuboid import*
from graphics.threeDgraphics.sphere import*

l=int(input("enter the length of rectangle:"))
b=int(input("enter the bredth of rectangle:"))
print("Area of rectangle =",RectArea(l,b),)
print("perimeter of rectangle :",RectPerimeter(l,b))


r=int(input("enter the radius of circle:"))
print("Circle area =",CirArea(r))
print("Circle Perimeter =",CirPerimeter(r))
print()

r=int(input("enter the radius of sphere:"))
print("area of sphere =",SphereArea(r))
print("Perimeter of sphere =",SpherePerimeter(r))
print()

l=int(input("enter the length of cuboid:"))
b=int(input("enter the bredth of cuboid:"))
h=int(input("enter the height of cuboid:"))
print("area of cuboid =",CubArea(l,b,h))
print("perimeter of cuboid =",CubPerimeter(l,b,h))



