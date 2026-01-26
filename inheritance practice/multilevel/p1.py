class Humain_being():
    def __init__(self):
        print("Humain being constructor called .")
        self.name = input("Enter your name : ")

class Employee(Humain_being):
    def __init__(self):
        super().__init__()
        print("Employee class constructor called :")
        self.salary = float(input("Enter your salary."))

class Manager(Employee):
    def __init__(self):
        super().__init__()
        print("Manager class constructor called.")
        self.bonus = float(input("Enter your bonus."))
    
    def display(self):
        print("name: ",self.name)
        print("salary : ",self.salary)
        print("bonus : ",self.bonus)
m1 = Manager()
m1.display()