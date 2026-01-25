class Father:
    def __init__(self):
        print("Father class constructor called: ")
        self.vehicle = "scooter"

class Son(Father):
    def __init__(self):
        print("son class construtor called:")
        self.vehicle = "BMW"
    
s = Son()
print(s.__dict__)
