class Employee:
    bonus = 2000
    def display(self):
        print("this is parent class : ")
class Manager(Employee):
    bonus1 = 1000
    def show(self):
        print("this is child class : ")
mg = Manager()
mg.display()
mg.show()
print(mg.bonus)
print(mg.bonus1)