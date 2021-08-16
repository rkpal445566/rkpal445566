class customer:
    
    

    def __init__(self,name,balane=0.00):
        self.name= name
        self.balane=balane

    
    def deposit(self,amount):
        self.balane=self.balane + amount
        print("total deposot amount",self.balane)
        print("****************************************")
       
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds not parfom this operaton")

        else:
               self.balane=self.balane - amount
               print("withdraw anount",self.balane) 
               print("************************************************")

    name=int(input("inter a name"))

obj=customer("name")
while True:
    print('d-deposit/n  w-withdraw/n  e-exit')

    option=int(input("choos your option"))
    if option.lower()=='d':
        amount=float(input("inte a amount deposit"))
        obj.deposit(amount)

    elif option.lower()=='w':
        amount=float(input("enter a wthdrw amount"))
        obj.withdraw(amount)

    elif option.lower()=='e':
        amount=float(input("enter a amount exit"))

    else:
        print("welcome to banke")
