import os
os.system("cls")
class Atm():
    def __init__(self,balance,pin,name):
        self.balance = balance
        self.name = name
        self.pin = pin

    def Checkbalance(self):
        print("Balance: "+ str(self.balance))
    def Withdraw(self):
        withd = int(input("Please enter amount you wish to withdraw"))
        if withd>self.balance:
            print("You cannot withdraw more amount than what is in your account")
        else:
            print("New Balance: "+str(self.balance - withd))
    def readName(self):
        print(self.name)
    def depositMoney(self):
        
        dep = int(input("Enter amount you wish to deposit"))
        self.balance += dep
        print("New Balance: "+str(self.balance))

store1 = Atm(500,1234,"Wyatt")


store1.depositMoney()

