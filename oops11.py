# method overriding.

class Square():
	def area(self,s):
		return s**2
class Rectangle(Square):
	def area(self,l,b):
		return l*b
sq = Square()
print(sq.area(5)) 

rect = Rectangle()
print(rect.area(4,5))