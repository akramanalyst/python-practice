class Person:
    def __init__(self,name,age,sal):
# private data
        self.__name = name
        self.__age = age
#protected data
        self._salary = sal
    def display(self):
        print(f"name is {self.__name} and age is {self.__age} and th salary of person is {self._salary}")
p = Person("Rehan",23,50000)
p.display()
