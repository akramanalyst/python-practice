class Employee:
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
emp =Employee('Akram',30000,25)
print(emp.__dict__)
print(getattr(emp,'salary'))
setattr(emp,'name','Jamal')
print(emp.__dict__)
print(hasattr(emp,'age'))
print(hasattr(emp,'id'))
delattr(emp,'age')
print(emp.__dict__)


