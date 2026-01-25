class Bank:
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = 0
    def deposit(self,amt):
        amt = int(input("Enter amount to deposit : "))
        if amt > 0:
            self.balance = self.balance+amt
            #print(f"tatal amount is {self.balance}")
        else :
            self.balance = self.balance

    def withdraw(self,amt):
        amt = int(input("Enter amount to withdraw : "))
        if amt< 0:
            print(f"balance is negative {self.balance}")
        elif amt > self.balance:
            print(f"insufficient balance : enter less amount : ")
        else:    
            self.balance = self.balance - amt
            #print(f"remaining balance {self.balance}")
    def enquiry(self,amt):
        print("Available balance in your account : ",self.balance)
    def display(self):
        print("account number : ",self.accno)
        print("name of customer : ", self.name)
        print("Available balance: ",self.balance)
    print("select operations :\n" 
           '1.deposit\n'\
           '2.wthdraw\n'\
           '3.Enquiry')
select = int(input("Enter options from 1 to 4 : "))
csacno = int(input("enter customer account no : "))
csname = input("Enter customer name : ")
amount = int(input(" : "))


b = Bank(csacno,csname,0)
if select ==1:
    print(b.deposit(amount))
elif select==2:
    print(b.withdraw(amount))
elif select ==3:
    print(b.enquiry(amount))
#b.deposit(amount)
#b.withdraw(amount)
b.display()

