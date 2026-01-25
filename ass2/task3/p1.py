# python program to create two functions area() and peri() to find and perimeter of rectangle.

n1  = int(input(" Enter first number : "))
n2  = int(input(" Enter second number : "))

def area(l,b):
	area = l*b
	print(area)

def peri(l,b):
	perimeter = 2*(l+b)
	print(perimeter)

area(n1,n2)
peri(n1,n2)