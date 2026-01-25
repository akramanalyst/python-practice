# python program to find out the volume and surface area of cuboid.

l = int(input("Enter the lenght of cuboid = "))
b = int(input("Enter the bridth of cuboid = "))
h = int(input("Enter the height of cuboid = "))

vol = l*b*h
print("volume of cuboid = ",vol)

sa = 2*(l*b+b*h+h*l)
print("surface Area of cuboid = ",sa)
