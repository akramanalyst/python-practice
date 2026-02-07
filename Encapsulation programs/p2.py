class Person:
    #difine constructor.
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def _display(self):
        print("name is : ",self._name)
        print("age is : ",self._age)

class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self._roll_no = roll_no
    
    def display(self):
        self._display()
        print("Rollnumber is : ",self._roll_no)

s = Student("Ariz",29,10003)
s.display()
        

 