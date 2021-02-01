import graphics.rectangle
print("---------rectangle-----------\n")
l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
print("area: ",graphics.rectangle.area(l,b))
print("perimeter: ",graphics.rectangle.perimeter(l,b))

from graphics.circle import area as a
from graphics.circle import perimeter as p
print("----------circle-----------\n")
r=int(input("enter the radius: "))
print("area: ",a(r))
print("perimeter: ",p(r))


from graphics.dgraphics.cuboid import area as a
from graphics.dgraphics.cuboid import perimeter as p
print("-----------cuboid---------\n")
l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
h=int(input("enter the height: "))
print("area: ",a(l,b,h))
print("perimeter: ",p(l,b,h))


from graphics.dgraphics.sphere import*
print("------------sphere----------\n")
r=int(input("enter the radius: "))
print("area: ",area(r))
print("circumference: ",circumference(r))
