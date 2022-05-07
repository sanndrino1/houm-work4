

#Проект 5 Управление на банкова сметка
#Описание:
#Проектът представлява обикновена банкова система. Той съдържа само
#административна част, без да се дава възможност на потребителя да влиза в система с
#потребителско име и парола. Административната част включва всички основни
#функции: създаване на нов акаунт, преглед на записа на притежателите на акаунти,
#теглене и депозит на сума, запитване за салдо. Потребителят трябва лесно да може да
#проверява общите записи на банковата сметка. Потребителят може да създаде акаунт,
#като предостави първоначална сума за депозиране. Той може да депозира и тегли пари
#само като предостави номера на потребителската си сметка и въведе сума.
#Потребителят може да проверява за клиенти и техният баланс по сметка.






from optparse import Option


class Bank_Account:
    count=0
    balance=0
    def __init__(self,balance,Number,Farst_Name,Secand_Name,Name,withdrawl,deposit):

        
        self.balance=balance
        self.balance=2000
        self.Number=Number
        self.Farst_Name=Farst_Name
        self.Secand_Name=Secand_Name
        self.Name=Name
        self.withdrawl=withdrawl
        self.deposit=deposit
    
 

    def get_input(self):
        self.Number=int(input('Enter Number :! '))
        self.Farst_Name=str(input('Enter Farst Name :! '))
        self.Secand_Name=str(input('Secand Name :! '))
        
        self.withdrawl+=float(input('Enter Whithdrawl :! '))
        self.deposit=int(input('Enter Deposit :! '))
   
        
    def get_Name(self):
        
        Name=(f' {self.Farst_Name} '+' '+f'{self.Secand_Name}')
        self.Name=Name
    def get_Number(self):
         
                if (self.Number == " "):
                    if 0 < len(self.Number)>=2:
                        print('False Numer')
                        
                else:
                    
                        self.Number=self.Number
                        print(f'Number is:{self.Number}')
    def get_balance(self):
        self.balance=self.balance-self.withdrawl
        
        if   self.withdrawl >self.balance:
            print(' Withdraw  is Biggest then Balance :!!!')
            print('stop :!exit()')
            
        return self.balance
    def get_deposit(self):
        self.deposit=self.balance + self.deposit
        self.balance -= self.withdrawl
        print(f'Current_balance :!! {self.balance}')
        return self.deposit
        
    
    def info(self):
        print(f' Number:{self.Number}  Farst Name:{self.Farst_Name}  Secand Name:{self.Secand_Name}   Withdrawl:{self.withdrawl}  Deposit:{self.deposit}  Balance:{self.balance}')
    
        print(f'....................................')
        print(f'........Total Acount:!..............')
        print(f'Acount Number:   :! {self.Number}')
        print(f'Full Name:       :!{self.Name}')
        print(f'Balance:         :!{self.balance}')
        print(f'Withdrawl:       :!{self.withdrawl}')
        print(f'Deposit:        :!{self.deposit}')
        print(f'...................................')
    
            
s = Bank_Account(1,'maria','geri',0,0,2000,0)

s.get_input()
s.get_Number()
s.get_Name()
s.get_balance()
s.get_deposit()
s.info()

           
          
  