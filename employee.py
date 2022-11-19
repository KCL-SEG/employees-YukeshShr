"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, pay, hours = 0, commission = 0, contractCom = 0):
        self.name = name
        self.contractType = contractType
        self.pay = pay
        self.hours = hours
        self.commission = commission
        self.contractCom = contractCom

    def get_pay(self):
        if(self.contractType == 'monthly'):
            return self.pay
        elif(self.contractType == 'hourly'):
            return self.hours * self.pay
        elif(self.contractType == 'monthly commission'):
            return self.pay + (self.commission * self.contractCom)
        elif(self.contractType == 'hourly commission'):
            return (self.hours * self.pay) + (self.commission * self.contractCom)
        elif(self.contractType == 'monthly bonus commission'):
            return (self.pay) + (self.commission)
        elif(self.contractType == 'hourly bonus commission'):
            return (self.hours * self.pay) + (self.commission)

    def __str__(self):
        if(self.contractType == 'monthly'):
            return f'{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.get_pay()}.'
        elif(self.contractType == 'hourly'):
            return f'{self.name} works on a contract of {self.hours} hours at {self.pay}/hour. Their total pay is {self.get_pay()}.'
        elif(self.contractType == 'monthly commission'):
            return f'{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.contractCom} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}.'
        elif(self.contractType == 'hourly commission'):
            return f'{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a commission for {self.contractCom} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}.'
        elif(self.contractType == 'monthly bonus commission'):
            return f'{self.name} works on a monthly salary of {self.pay} and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}.'
        elif(self.contractType == 'hourly bonus commission'):
            return f'{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a bonus commission for {self.commission}. Their total pay is {self.get_pay()}.'
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', '4000')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly commission', 3000, commission = 200, contractCom = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly commission', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly bonus commission', 2000, commission= 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly bonus commission', 30, 120, 600)
