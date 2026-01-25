class Father:
    def __init__(self):
        print("Father constructor called : ")
        self.vehicle = "Scooter"

class Son(Father):
    pass
s = Son()
print(s.__dict__)