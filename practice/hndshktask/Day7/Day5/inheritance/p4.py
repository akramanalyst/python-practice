class Computer:
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("computer class constructor called.")

class Mobile(Computer):
    def __init__(self, ram, storage):
        super().__init__(ram, storage)
        self.model = "iphone x"
        print("mobile class constructor called.")
mob = Mobile('8gb','512gb')
print(mob.__dict__)