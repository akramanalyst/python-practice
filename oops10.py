"""
polymorphism.

# "poly" = many and "morph" = forms
# the concept of defining multiplelogics to perform some operation is known as a polyorphism.

types of polymorphism.
1.method oevrloading

2.mehtod overriding.

int+int=arithmatic
str+str=concatinate
""" 
#python do not support method overloading natively.
#method overloading 
class shape:
	#method over loading by default parameter.
	def area(self,a=None,b=None):
		if a is not None and b is None:
			return a**2
		elif a is not None and b is not None:
			return a*b


	#method over loading by variable length arguments.
	def area(self,*args):
		if len(args)==1:
			return args[0]**2
		elif len(args)==2:
			return args[0]*args[1]
sq = shape()
print("area of square = " ,sq.area(5))
print("area of rectangle = ", sq.area(5,6))