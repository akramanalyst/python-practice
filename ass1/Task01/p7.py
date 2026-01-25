# python program to find out Area and perimeter of circle and taking input from users.
# r ( radius of circle ) is variable which is hold the memory address.

r = int(input("Enter the radius of circle = "))
area = 3.14*r*r
print("Area of circle =  " , area)
print(type(area))

peri = 2*3.14*r
print("perimeter of circle = ", peri)
print(type(peri))