class Bank_Account:
    company = "Axis Bank"
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account

    def debit(self,amount):
       # print("msg from the bank : ",self.company)
        self.balance -= amount 
        print("Rs.", amount ,"has been debited")
        print("total available balance in your account : ",self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount ,"has been credited") 
        print("total available balance in your account : ", self.get_balance())
              
    def get_balance(self):
         return self.balance

acc1 = Bank_Account(100000,1326)
print(Bank_Account.company)
acc1.debit(10000)
acc1.credit(5000)
acc1.credit(50000)
acc1.debit(12000)