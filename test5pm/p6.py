'''
 wap to create class named Employee create a constructor to initialize empid
empname,variables and display () method to dislay values.
test class for three employees.
'''
class Employee:
	def __init__(self,empid,empname):
		self.id = empid
		self.name = empname
	def display(self):
		print("empid : ",self.id)
		print("empname : ", self.name)

e1 = Employee(1002,'Akram')
e2 = Employee(1003 , 'Ramesh')
e3 = Employee(1004 , 'Amir')
e1.display()
e2.display()
e3.display()
