'''
# with constructor
class myclass :
	def __init__(self):
		self.name = 'Akram Jamal'
	def sayHello(self ):
		print(" Hello !" ,self.name )

c = myclass()
c.sayHello()
'''
# without constructor.
class myclass : 
	def sayHello(self,name):
		self.name = name
		print("Hello ! ",self.name)
name = input("Enter name : ")
c = myclass()
c.sayHello(name)