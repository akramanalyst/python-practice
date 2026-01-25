
class Rectangle():
	def __init__(self,l ,b):
		self.length = l
		self.breadth = b
	def area(self):
		return self.length*self.breadth
rec = Rectangle(6,5)
print("Area of rectangle : ",rec.area())
