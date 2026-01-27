class Person:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag
    def display(self):
        print('Person class called.')
        print('name :',self.name)
        print('Age : ',self.age)
         
        
class Employee(Person):
    def __init__(self,nm,ag,sal):
        super().__init__(nm,ag)
        self.salary = sal
    def display1(self):
        print('Employee class called.') 
        print('name :',self.name)
        print('Age : ',self.age)
        print('employee  salary:',self.salary)
        
class Student(Person):
    def __init__(self,nm,ag,mr):
        super().__init__(nm,ag)
        self.marks = mr
    def display2(self):
        print('student class called.')
        print('name :',self.name)
        print('Age : ',self.age)
        
        print("student marks: ",self.marks)


s1 =Student('Asif',28,80)
e1 =Employee('Ratnesh',27,50000)
p1 = Person('Rehan',25)
s1.display2()
e1.display1()
p1.display()