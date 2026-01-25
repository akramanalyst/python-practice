class Employee:
    company_name = 'wipro'
    def __init__(self,eid,ename):
        self.id = eid
        self.name = ename
    @classmethod
    def get_company(cls):
        print(cls.company_name)
        cls.company_name = 'infosys'
        print(cls.company_name)

e1 = Employee(10002,'Akram')
Employee.get_company()
print(e1.company_name)