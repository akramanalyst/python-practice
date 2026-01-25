
'''
class Employee:
	def setEmployee(self,id ,name,salary):
		self.id = id
		self.name = name
		self.salary = salary
	def display(self):
		print("employee id  : ",self.id)
		print("employee name : " ,self.name)
		print("employee salary ",self.salary)
empid = int(input("Enter Employee id : "))
empname = input("Enter Employee name : ")
salary = int(input("Enter Employee salary : "))
e = Employee()
e.setEmployee(empid,empname,salary)
#e.setEmployee(1009,'akram',80000)
e.display()
'''

class Employee() :
	def __init__(self,id,name,salary):
		self.id = id
		self.name = 'name'
		self.salary = salary
	def display(self):
		print("Employee id ",self.id)
		print("Employee name",self.name)
		print("Employee salary" ,self.salary)
empid = int(input("Enter Employee id : "))
empname =input("Enter Employee name : ")
empsalary = int(input("Enter Employee salary : "))
e = Employee(empid,empname,empsalary)
e.display()