# Method Overriding Examples.
class A:
    def ShowData(self):
        print("I am class A : ")
    
class B(A):
    def ShowData(self):
        super().ShowData()
        print("I am class B : ")

obj = B()
obj.ShowData()