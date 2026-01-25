
#Destructor.
#Destructor is a special type of method which is use to destroy the object and free the resources used by it.

class Myclass():
	def __init__(self,name):
		self.name = name	
		print("object is  created and data is stored")
	def sayhello(self):
		print("HI")
	def _del_(self):
		print(f"{self.name} object is destroyed")
	def _str_(self):
		return self.name

obj1 = Myclass("aman")
obj1.sayhello()
print(obj1)
