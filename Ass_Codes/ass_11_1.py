'''
Q. Write a python class Bank. Derive class custumer from the base class bank .Create new account for a customer and handle basic banking operations deposit and withdraw.
''' 
class bank:
    def _init_(self):
        self.cn=" "
        self.ca=""
        self.an=0
        self.cb=0
    def acc_create(self,cn,ca,an,cb):
        self.cn=cn
        self.ca=ca
        self.an=an
        self.cb=cb
    def chbl(self):
        print("Custumer name :",self.cn)
        print("Custumer Address :",self.ca)
        print("Custumer A/C :",self.an)
        print("Custumer bank Balance :",self.cb)
    def upbl(self):
        print("Custumer updated balance :",self.cb)
class cust(bank):
    def withdraw(self,amt):
        self.cb=self.cb-amt
    def deposit(self,amt):
        self.cb=self.cb+amt
ob=cust()
choice=0
while(choice!=5):
    choice=int(input('''1. Create account 2.Check bal 3. Deposit 4. Withdraw 5. Exit\n'''))
    if (choice==1):
        cn=input("Enter name : ")
        ca=input("Enter address : ")
        an=eval(input("Enter A/C :"))
        cb=eval(input("Enter Initail Balance :"))
        ob.acc_create(cn,ca,an,cb)
    if (choice==2):
        ob.chbl()
    if (choice==3):
        amt=eval(input("Enter amount to deposit :"))
        ob.deposit(amt)
        ob.upbl()
    if (choice==4):
        amt=eval(input("Enter amount to withdraw :"))
        ob.withdraw(amt)
        ob.upbl()

