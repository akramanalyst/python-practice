class student :
    def __init__(self,rollno,name,fee):
        self.rollno = rollno
        self.name = name
        self.fee = fee
    def display(self):
        print("student roll no : ",self.rollno)
        print("student name : ",self.name)
        print("student fee : ",self.fee)
enrol = int(input("Enter roll no of student : "))
name  = input("Enter student name : ")
fee = int(input("Enter the fee of students : "))
std =student(enrol,name,fee)
std.display()