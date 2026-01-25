class Bank:
    bank_name = 'SBI'
    rate_of_interest = 12.25
    @staticmethod
    def simple_interest(p,n):
        si = (p*n*Bank.rate_of_interest)/100
        print(si) 
p = float(input("enter the principle values : "))
n = int(input("enter the no.of years :"))
Bank.simple_interest(p,n)

